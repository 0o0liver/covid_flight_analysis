### To run this, please use: `python test.py 'New York City'`
### You can change the city as you want

from urllib.request import urlopen
from io import StringIO
import csv

import matplotlib.pyplot as plt
import sys

data = urlopen("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
rows = [row for row in csvReader]


city = sys.argv[1]
total_num = []
death_case = []
Date = []
count = 0

for item in rows:
	if item[1] == city:
		count += 1
		total_num.append(int(item[-2]))
		death_case.append(int(item[-1]))
		if count%3==1:
			Date.append(item[0][-5:])
		else:
			Date.append('')

X = [i+1 for i in range(count)]

plt.title("Data in %s" %(city))
plt.xlabel("date")
plt.ylabel("number")

plt.plot(X, total_num, 'r', label='cases')
plt.plot(X, death_case, 'b', label='deaths')
plt.scatter(X, total_num, marker='o', color='black', s=20)
plt.scatter(X, death_case, marker='o', color='black', s=20)
plt.xticks(X, Date, rotation=90)

plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()


'''
different_cities = []
for item in rows:
	if item[1] not in different_cities:
		different_cities.append(item[1])
different_cities.sort()

print("The number of cities is:", len(different_cities))
print(different_cities)
'''


