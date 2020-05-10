# COVID_Flight_Analysis

|     Team Name    |
|------------------|
|Airline with COVID|

| Team Member      | NetId|
|------------------|------|
| Shantanu Tripathi|st3810|
|         Dongzi Qu| dq394|
|        Binghan Li|bl1890|

# Introduction
COVID-19 is spreading widely and rapidly across the globe, from China to Europe, and now to the United States. Within the United State, the deadly virus has infected every state in less than a month. One of the reasons for such insane spreading, on top of the level of contagiousness of COVID-19, is frequent air travel. There are over one million flights happening every day worldwide, it is currently the fastest way for humans to travel to anywhere in the world, unfortunately, it is for the virus as well. Additionally, aircrafts create an environment that is beneficial for COVID-19 to spread, over 100 passengers are in a sealed cabin together for hours without a medical grade ventilation system, if one passenger is infected with the virus, it is highly possible, if not 100 percent, for other passengers to become infected. With this information in everyone’s mind, our team wants to discover how the air travel industry is being affected by COVID-19 within the United States. Furthermore, we want to utilize data to trace the origin of the virus for cities in the United States. Hope you enjoy our project!

# Datasets used

## Raw Data
* **us-counties.csv**: This dataset contains county level COVID-19 information in the United States, and it is updated daily by New York Times. Columns of interest are date, county, state, cases and deaths. This dataset can be viewed and downloaded from [here](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv).
* **Flights**: This dataset contains worldwide flight information within the first 4 months of 2020, and it consists of 4 data files, each data file contains 1 month of flight information. This dataset is provided by OpenSky Network for combating COVID-19, and it is updated monthly. This dataset can be downloaded [here](https://opensky-network.org/datasets/covid-19/).
* **airports.csv**: This dataset contains information for every airport in the world, and it is provided and maintained daily by OurAirports. This dataset is used for elaborating flight information, such as adding county and state information for destination airport and origin airport for interested flights. This dataset can be downloaded [here](https://ourairports.com/data/airports.csv).

## Generated Data

* **inter_city_flight_data.csv**: This dataset records the details about different flights on different days. 
Dataset looks like:
```
+--------------------+------------+---------+----------+----------+             
|           from_city|from_airport|  to_city|to_airport|       day|
+--------------------+------------+---------+----------+----------+
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-15|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-17|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-21|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-21|
+--------------------+------------+---------+----------+----------+
```

* **covid_flight_count_data.csv**: For every city, this dataset, records the daily count of COVID cases/deaths and number of flights flying to and fro from that city on that particular day. 
Dataset looks like:

```
Flight and Covid daily count on merged_flight.csv:
+------+----------+-----+------+---------------------+---------------------+    
|  city|       day|cases|deaths|incoming_flight_count|outgoing_flight_count|
+------+----------+-----+------+---------------------+---------------------+
|BOSTON|2020-02-01|    1|     0|                  341|                  310|
|BOSTON|2020-02-02|    1|     0|                  299|                  293|
|BOSTON|2020-02-03|    1|     0|                  395|                  405|
|BOSTON|2020-02-04|    1|     0|                  423|                  424|
+------+----------+-----+------+---------------------+---------------------+
```
# How to generate the resultant data using all the detailed steps: (Long Process) #

1. Get the raw data by referring to the Readme file of the Datasets folder: https://github.com/shantanutrip/covid_flight_analysis/tree/master/Datasets

2. On this raw data, run the driver.py script. For this, refer to the Readme file of the Code folder: https://github.com/shantanutrip/covid_flight_analysis/tree/master/Code

# How to generate the resultant data by using the already made raw data: (Short Process) #

1. Since we have already made the raw data, the user can upload the following datasets to the hfs: <br>
  a. [disease.csv](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/disease.csv) <br>
  b. [merged_flight.csv](https://drive.google.com/file/d/1NU0pVbESGXNOVja2vs4yxGaWe9khz728/view?usp=sharing) <br>
  c. [airports.csv](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/airports.csv) <br>
  d. [city_list.csv](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/city_list.csv) <br>
  e. [map_list.csv](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/map_list.csv) <br>

2. Follow steps from the Readme file of the Code folder: https://github.com/shantanutrip/covid_flight_analysis/tree/master/Code.
