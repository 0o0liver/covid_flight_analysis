# covid_flight_analysis

An attempt to analyse the affect of flights on the spread of COVID and vice versa

**Link to the Reslutant Datasets:** https://github.com/shantanutrip/covid_flight_analysis/tree/master/Resultant_Data

## Deatils of the datasets being generated: ##

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
# How to generate the resultant data using the repo: #

1. Get the raw data by referring to the Readme file of the Datasets folder: https://github.com/shantanutrip/covid_flight_analysis/tree/master/Datasets

2. On this raw data, run the driver.py script. For this, refer to the Readme file of the Code folder: https://github.com/shantanutrip/covid_flight_analysis/tree/master/Code
