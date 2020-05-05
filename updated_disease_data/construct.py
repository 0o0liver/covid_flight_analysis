from urllib.request import urlopen
from io import StringIO
import csv

import sys
import pandas as pd

## Get the original data from this webpage
data = urlopen("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
rows = [row for row in csvReader]

## Months users want
months = sys.argv[1].split(',')

## Cities users want
f = open('city_list.csv', 'r')
lines = f.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip('\n')

## Store the data
Database = []
Column = ['City', 'Date', 'Cases', 'Deaths']
for row in rows:
	if row[0][-5:-3] in months:
		temp = row[1] + ',' + row[2]
		if temp in lines:
			Database.append([row[1], row[0], row[4], row[5]])
Database = sorted(Database, key=(lambda x:[x[0], x[1]]))

## Export the data
Export_Data = pd.DataFrame(columns=Column, data=Database)
Export_Data.to_csv('disease.csv', index=False)