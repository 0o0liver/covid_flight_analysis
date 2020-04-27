import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":

	# Gather target city name
	cityList = []
	cityFile = open(sys.argv[2], "r")
	for line in cityFile:
		cityList.append(line.rstrip().upper())

	# Read in flight and airport file
	spark = SparkSession.builder.appName("build_dataset").getOrCreate()
	AllFlight = spark.read.format("csv").options(header="true").load(sys.argv[1])
	Airports = spark.read.format("csv").options(header="true").load("airports_cleaned.csv")

	TargetAirports = Airports.filter((Airports["municipality"].isin(cityList)) & ((Airports["type"]=="large_airport") | (Airports["type"]=="medium_airport"))).select(Airports["ident"], Airports["name"], Airports["municipality"])
	TargetAirports.show()

	# Outgoing flight count from target city each day
	Outgoing = TargetAirports.join(AllFlight, (AllFlight.origin==TargetAirports.ident)).groupby("municipality", "day").count().orderBy("municipality", "day").withColumnRenamed("count", "OutgoingCount")

	# Incoming flight count at target city each day
	Incoming = TargetAirports.join(AllFlight, (AllFlight.destination==TargetAirports.ident)).groupby("municipality", "day").count().orderBy("municipality", "day").withColumnRenamed("count", "IncomingCount").withColumnRenamed("municipality", "Imunicipality").withColumnRenamed("day", "Iday")

	# Join incoming and outgoing
	result = Outgoing.join(Incoming, (Outgoing.municipality==Incoming.Imunicipality) & (Outgoing.day==Incoming.Iday)).drop(Incoming.Imunicipality).drop(Incoming.Iday).orderBy("municipality", "day")
	result.show()
	result.toPandas().to_csv("flightCount.csv", header=True, index=False)
