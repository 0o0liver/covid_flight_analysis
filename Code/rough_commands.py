from csv import reader

MUNI = 10
TYPE = 2

def processString(input_string):
	if input_string == None:
		return input_string
	return input_string.lstrip().rstrip().upper()

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
	schema = airport.mapPartitions(lambda line: reader(line)).take(1)[0]
	valid_data = airport \
				.mapPartitions(lambda line: reader(line)) \
				.map(lambda arr: [processString(x) if i != MUNI else findMapping(processString(x)) for i,x in enumerate(arr)]) \
				.filter(lambda arr: arr[MUNI] in city_list and arr[TYPE] in airport_type_list) \
				.collect()
	return spark.createDataFrame(valid_data, schema)

city_mapper = getCityMapper('Datasets/map_list.csv')
city_list = getCityList('Datasets/city_list.csv')
airport_type_list = getAirportTypeListFor(['medium_airport','large_airport'])
aiport_dataframe = getAirportDataDFrame('Datasets/airports.csv')

