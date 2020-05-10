from urllib.request import urlopen
from io import StringIO
import csv

import sys
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

data = urlopen("https://raw.githubusercontent.com/shantanutrip/covid_flight_analysis/master/Resultant_Data/covid_flight_count_data.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
rows = [row for row in csvReader if row[0]!='city']

city_list = []
for row in rows:
	if row[0] not in city_list:
		city_list.append(row[0])

def save_image_1(city_name):
	temp = city_name

	flight_in = []
	flight_out = []
	flight_all = []
	total_num = []
	Date = []
	count = 0

	for row in rows:
		if row[0] == temp:
			count += 1
			flight_in.append(int(row[4]))
			flight_out.append(int(row[5]))
			flight_all.append(int(row[4])+int(row[5]))
			total_num.append(int(row[2]))
			if count%3==1:
				Date.append(row[1][-5:])
			else:
				Date.append('')

	X = [i+1 for i in range(count)]

	plt.title("Data in %s" %(temp))
	plt.xlabel("date")
	plt.ylabel("number")

	plt.plot(X, total_num, 'r', label='cases')
	plt.plot(X, flight_in, 'b', label='flight_in')
	plt.plot(X, flight_out, 'g', label='flight_out')
	plt.plot(X, flight_all, 'y', label='flight_all')
	plt.scatter(X, total_num, marker='o', color='black', s=10)
	plt.scatter(X, flight_in, marker='o', color='black', s=10)
	plt.scatter(X, flight_out, marker='o', color='black', s=10)
	plt.scatter(X, flight_all, marker='o', color='black', s=10)
	plt.xticks(X, Date, rotation=90)

	plt.legend()
	#plt.grid()

	plt.savefig('image_1/%s.jpg' % temp, dpi=300)

	plt.close()

for city_name in city_list:
	save_image_1(city_name)
