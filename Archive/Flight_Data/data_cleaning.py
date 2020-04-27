from pyspark import SparkContext

def convertUpper(lines):
	lst = lines.split(",")
	if lst[10] == '"municipality"':
		return lines
	lst[10] = lst[10].upper()
	return ",".join(lst)

if __name__ == "__main__":
	sc = SparkContext()	

	# Cleaning airport data. Change municipality to uppercase
	airports = sc.textFile("airports.csv", 1)
	airports.map(convertUpper).saveAsTextFile("airports_cleaned")
