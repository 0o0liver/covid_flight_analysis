# COVID Flight Analysis

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
* **airports.csv**: This dataset contains information for every airport in the world, and it is provided and maintained daily by OurAirports. This dataset is used for elaborating flight information, such as adding county and state information for destination airport and origin airport for interested flights. This dataset can be downloaded [here](https://ourairports.com/data/airports.csv), and it is also provided in this repo at [here](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/airports.csv).

## Generated Data

* **disease.csv**: This dataset is generated from [```us-counties.csv```](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv) using [```construct.py```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Code/construct.py). This dataset contains COVID-19 information for interested counties, which is listed in [```city_list.csv```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/city_list.csv). Generation instruction is provided [here](https://github.com/shantanutrip/covid_flight_analysis/tree/master/Datasets#diseasecsv). Complete dataset can be found [here](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/disease.csv). Sample dataset is provided below.
```
+--------------------+-----------+------------+    
|     City|      Date|      Cases|      Deaths|
+--------------------+-----------+------------+
|Allegheny|2020-03-14|          1|           0|
|Allegheny|2020-03-15|          3|           0|
|Allegheny|2020-03-16|          5|           0|
|Allegheny|2020-03-17|         10|           0|
+--------------------+-----------+------------+
```

* **merged_flight.csv**: This dataset is generated from all 4 flight data files, it keeps all columns from the original datafiles. This dataset is generated to benefit our analytic models to easily load flight information without having to deal with multiple data files. Generation instruction is provided [here](https://github.com/shantanutrip/covid_flight_analysis/tree/master/Datasets#merged_flightcsv). Complete dataset can be found [here](https://drive.google.com/file/d/1NU0pVbESGXNOVja2vs4yxGaWe9khz728/view?usp=sharing).

* **inter_city_flight_data.csv**: This dataset contains information for every flight between cities listed in [```city_list.csv```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/city_list.csv). It is generated from [```merged_flight.csv```](https://drive.google.com/file/d/1NU0pVbESGXNOVja2vs4yxGaWe9khz728/view?usp=sharing) using [```driver.py```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Code/driver.py). Generation instruction is provided [here](https://github.com/shantanutrip/covid_flight_analysis/tree/master/Code#driverpy-to-generate-the-desired-datasets). Complete dataset can be found [here](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Resultant_Data/inter_city_flight_data.csv). Sample dataset is provided below.
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

* **covid_flight_count_data.csv**: This dataset contains information for every city listed in [```city_list.csv```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/city_list.csv), for every date since the spread on COVID-19 in that city, the number of COVID-19 cases and deaths, as well as the amount of incoming and outgoing flights. This data is generated from [```merged_flight.csv```](https://drive.google.com/file/d/1NU0pVbESGXNOVja2vs4yxGaWe9khz728/view?usp=sharing), [```airports.csv```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/airports.csv) and [```disease.csv```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/disease.csv). Generation instruction is provided [here](https://github.com/shantanutrip/covid_flight_analysis/tree/master/Code#driverpy-to-generate-the-desired-datasets). Complete dataset can be found [here](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Resultant_Data/covid_flight_count_data.csv). Sample dataset is provided below.
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
# Data Cleaning

## Challenges
* COVID-19 dataset is county level data, but airports dataset only provides the city name of the location of each airport. For example, “KHOU” is the airport code for William P. Hobby Airport which is located in Houston Texas. However, in COVID-19 dataset, Houston Texas is not an entry because Houston is not a county, instead Harris Texas is used in COVID-19 datasets.
* Inconsistent city naming convention for airports data and COVID-19 data. For example, in airports dataset, "New York" is the city name of JFK, however, in COVID-19 dataset, "New York City" is the name for New York.
* Flight data is provided in four data files with different formats, they need to be merged together for it to be easily loaded for our analytic models.

## Process
* To address the issue of different spatial resolution, we used the geopy library to calculate the county information using each airport’s coordinates.
* To address the issue of different naming conventions, we constructed the [```map_list.csv```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/map_list.csv) for the cities listed in [```city_list.csv```](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/city_list.csv), it contains pairs of names that are different but representing the same city. Beyond the scope of this project, we would have to use geopy to standardize names.  

# Analysis

## COVID-19 Impacts Air Travel Industry:
As expected, the air travel industry is being negatively impacted by COVID-19. We came to this conclusion by plotting the number flights along with the COVID-19 cases number for each interested city over the course of the pandemic. It clearly shows that the amount of flights decreases dramatically as the number of COVID-19 cases increases. Below is a sample plotting for the city of San Francisco. Complete set of graphs can be found [here](https://github.com/shantanutrip/covid_flight_analysis/tree/master/Analysis/COVID_vs_Flight_Graphs). Reproducible implementation of such a task can be found [here](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Analysis/Analysis_Filght_Covid_Colab.ipynb).
![Sample plotting](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Analysis/COVID_vs_Flight_Graphs/SAN%20FRANCISCO.jpg)

