# COVID_Flight_Analysis

An attempt to analyse the affect of air travel on the spread of COVID and vice versa

|     Team Name    |
|------------------|
|Airline with COVID|

| Team Member Name | NetId|
|------------------|------|
| Shantanu Tripathi|st3810|
|         Dongzi Qu| dq394|
|        Binghan Li|bl1890|


**Link to the Reslutant Datasets:** https://github.com/shantanutrip/covid_flight_analysis/tree/master/Resultant_Data

## Details of the datasets being generated: ##

### The repo helps in making the 2 clean datasets that will be used for further analysis. The resultant datasets are: ###

1. `inter_city_flight_data.csv` : This dataset records the details about different flights on different days. 
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

2. `covid_flight_count_data.csv` : For every city, this dataset, records the daily count of COVID cases/deaths and number of flights flying to and fro from that city on that particular day. 
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
