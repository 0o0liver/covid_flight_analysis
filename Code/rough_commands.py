from csv import reader

MUNI = 10
TYPE = 2
ORIGIN = 5
DEST = 6
IDENT = 1 #ident
GST_CODE = 12
COUNTY = 1

def processString(input_string):
	if input_string == None:
		return input_string
	return input_string.lstrip().rstrip().upper()

def getSqlList(lst):
	return "(\""+'\",\"'.join(lst)+"\")"

def getAirportTypeListFor(temp_list):
	return [processString(x) for x in temp_list]

def getCityMapper(filename):
	city_map = {}
	mapper_rdd = sc.textFile(filename)
	mapper_list = mapper_rdd \
					.map(lambda line: (processString(line.split(',')[0]),processString(line.split(',')[1]))) \
					.collect()
	for key, val in mapper_list:
		city_map[key] = val
	return city_map

def findMapping(city_string):
	city_string = processString(city_string)
	if city_string in city_mapper:
		return city_mapper[city_string]
	return city_string

def getCityList(filename):
	city_rdd = sc.textFile(filename)
	city_list = city_rdd\
		.map(lambda line: (findMapping(processString(line.split(',')[0])), 1)) \
		.reduceByKey(lambda x,y: x + y) \
		.map(lambda x: x[0]) \
		.collect()
	return city_list

def getAirportDataDFrame(filename):
	airport = sc.textFile(filename)
	schema = ['ident','type','municipality','gst_code']
	valid_data = airport \
		.mapPartitions(lambda line: reader(line)) \
		.map(lambda arr: [processString(x) if i != MUNI else findMapping(processString(x)) for i,x in enumerate(arr)]) \
		.filter(lambda arr: arr[TYPE] in airport_type_list and arr[IDENT] != '' and arr[MUNI] != '' and arr[GST_CODE] != '') \
		.map(lambda arr: [arr[IDENT], arr[TYPE], arr[MUNI], arr[GST_CODE]]) \
		.collect()
	return spark.createDataFrame(valid_data, schema)

def getAllAirportCodes():
	airport_dataframe.registerTempTable('airport_df')
	df1 = sqlContext.sql ( 
			"""
				SELECT DISTINCT gst_code
				FROM airport_df
			"""
	)
	res = df1.collect()
	return [x['gst_code'] for x in res]

def getOnlyCityListAirportCodes():
	airport_dataframe.registerTempTable('airport_df')
	df1 = sqlContext.sql ("""
		SELECT DISTINCT gst_code 
		FROM airport_df 
		WHERE municipality in """ + getSqlList(city_list))
	res = df1.collect()
	return [x['gst_code'] for x in res]

def getCovidDataFrame(filename):
	covid = sc.textFile(filename)
	valid_data = covid \
		.mapPartitions(lambda line: reader(line)) \
		.map(lambda arr: [processString(x) if i != COUNTY else findMapping(processString(x)) for i,x in enumerate(arr)]) \
		.filter(lambda arr: arr[COUNTY] in city_list and arr[0] >= '2020-03-01') \
		.map(lambda arr: [arr[0], arr[1], arr[4], arr[5]]) \
		.collect()
	schema = ['date', 'county', 'cases', 'deaths']
	return spark.createDataFrame(valid_data, schema)

def getFlightDataFrame(filename):
	flight = sc.textFile(filename)
	valid_data = flight \
		.mapPartitions(lambda line: reader(line)) \
		.map(lambda arr: [processString(x) for x in arr]) \
		.filter(lambda arr: (
				arr[0] != 'CALLSIGN' and 
				arr[ORIGIN] != '' and 
				arr[DEST] != '' and 
				arr[ORIGIN] != arr[DEST] and
				(arr[ORIGIN] in only_city_list_airport_codes or arr[DEST] in only_city_list_airport_codes) and
				arr[ORIGIN] in all_airport_codes and 
				arr[DEST] in all_airport_codes
			)
		) \
		.map(lambda arr: [arr[ORIGIN], arr[DEST], arr[-1].split(' ')[0]]) \
		.collect()
	schema = ['origin', 'destination', 'day']
	return spark.createDataFrame(valid_data, schema)

def getInterCityFlightDataFrame():
	covid_dataframe.registerTempTable('covid_df')
	flight_dataframe.registerTempTable('flight_df')
	airport_dataframe.registerTempTable('airport_df')
	return sqlContext.sql(
	"""
		SELECT a1.municipality as from_city,
		d.from_airport as from_airport,
		d.to_city as to_city,
		d.to_airport as to_airport,
		d.day as day
		FROM airport_df as a1
		INNER JOIN (
			SELECT f.origin as from_airport,
			a2.municipality as to_city,
			f.destination as to_airport,
			f.day as day
			FROM airport_df as a2
			INNER JOIN flight_df as f
			ON a2.ident = f.destination
		) as d
		ON a1.ident = d.from_airport
	"""
	)

city_mapper = getCityMapper('Datasets/map_list.csv')
city_list = getCityList('Datasets/city_list.csv')
airport_type_list = getAirportTypeListFor(['medium_airport','large_airport'])
airport_dataframe = getAirportDataDFrame('Datasets/airports.csv')
all_airport_codes = getAllAirportCodes()
only_city_list_airport_codes = getOnlyCityListAirportCodes()
flight_dataframe = getFlightDataFrame('Datasets/merged_flight.csv')
covid_dataframe = getCovidDataFrame('Datasets/us-counties.csv')
inter_city_flight_dataframe = getInterCityFlightDataFrame()

