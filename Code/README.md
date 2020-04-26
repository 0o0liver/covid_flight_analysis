# Driver code to generate the desired datasets #

### The driver.py helps in making the 2 clean datasets that will be used for further analysis. The resultant dataset are: ###

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

## How to run the script: ##

To run the script, we need to go through the process of making initial datasets. The process is mentioned on https://github.com/shantanutrip/covid_flight_analysis/tree/master/Datasets.

After we successfully get the initial data using the link above, we will have the following data on our hfs:
1. disease.csv
2. airports.csv
3. city_list.csv
4. map_list.csv
5. merged_flight.csv

Once we have the above files in hfs, we can run the script.

**The only script we will be running is driver.py.**

The **input** of the script will be the **5 initial datasets i.e. disease.csv, airports.csv, city_list.csv, map_list.csv and merged_flight.csv**.

The **output** of the script will be 2 dataset folders which will  be saved by the script on hfs. The datasets will be called **inter_city_flight_data.out** and **covid_flight_count_data.out**.


We need to follow the given steps:
1. Clone the repository and upload https://github.com/shantanutrip/covid_flight_analysis/blob/master/Code/driver.py on your hpc VM. 

***Note, from step 2 onwards (including step 2), all the commands will be typed on the hpc VM.***

2. To begin with, let us remove any folders on hfs that have the same name as our resultant datasets: 
  a.```hfs -rm -r covid_flight_count_data.out``` 
  b.```hfs -rm -r inter_city_flight_data.out```

3. The following command will take 5 to 10 minutes to run. This is because one of the input datasets is huge.
```
spark-submit --conf \
spark.pyspark.python=/share/apps/python/3.6.5/bin/python \
driver.py \
<hfs path to map_list.csv> \
<hfs path to city_list.csv> \
<hfs path to airports.csv> \
<path to merged_flight.csv> \
<path to disease.csv>
```
For eg., if all the above datasets exist in ```Datasets/``` folder on hfs, the command would look like:
```
spark-submit --conf \
spark.pyspark.python=/share/apps/python/3.6.5/bin/python \
driver.py \
Datasets/map_list.csv \
Datasets/city_list.csv \
Datasets/airports.csv \
Datasets/merged_flight.csv \
Datasets/disease.csv
```

4. 
Once the data is successfully made on hfs, we can get the merged file to our hpc VM using the following commands:

```hfs -getmerge inter_city_flight_data.out data_intercity_with_multiple_headers.csv```
```hfs -getmerge covid_flight_count_data.out data_covid_with_multiple_headers.csv```

5. The files we have received have multiple headers and we want to get rid of them using the following commands:

```awk 'BEGIN{f=""}{if($0!=f){print $0}if(NR==1){f=$0}}' data_intercity_with_multiple_headers.csv > inter_city_flight_data.csv```
```awk 'BEGIN{f=""}{if($0!=f){print $0}if(NR==1){f=$0}}' data_covid_with_multiple_headers.csv > covid_flight_count_data.csv```

6. We can remove the files with multiple headers:
```rm data_covid_with_multiple_headers.csv```
```rm data_intercity_with_multiple_headers.csv```

7. Your current directory in the hpc cluster has the following 2 resultant dataset files: 
```inter_city_flight_data.csv```
```covid_flight_count_data.csv```

The datasets are present in the following
https://github.com/shantanutrip/covid_flight_analysis/tree/master/Resultant_Data

```
covid_dataframe:
+-----------+----------+-----+------+
|       city|      date|cases|deaths|
+-----------+----------+-----+------+
|SAN ANTONIO|2020-02-12|    1|     0|
|SAN ANTONIO|2020-02-13|    2|     0|
|SAN ANTONIO|2020-02-14|    2|     0|
|SAN ANTONIO|2020-02-15|    2|     0|
|SAN ANTONIO|2020-02-16|    2|     0|
|SAN ANTONIO|2020-02-17|    2|     0|
|SAN ANTONIO|2020-02-18|    2|     0|
|SAN ANTONIO|2020-02-19|    2|     0|
|SAN ANTONIO|2020-02-20|    2|     0|
|SAN ANTONIO|2020-02-21|    4|     0|
|SAN ANTONIO|2020-02-22|    4|     0|
|SAN ANTONIO|2020-02-23|    4|     0|
|SAN ANTONIO|2020-02-24|   10|     0|
|SAN ANTONIO|2020-02-25|   10|     0|
|SAN ANTONIO|2020-02-26|   10|     0|
|SAN ANTONIO|2020-02-27|   10|     0|
|SAN ANTONIO|2020-02-28|   11|     0|
|SAN ANTONIO|2020-02-29|   11|     0|
|SAN ANTONIO|2020-03-01|   11|     0|
|SAN ANTONIO|2020-03-02|   11|     0|
+-----------+----------+-----+------+

airport_dataframe:
+-------+--------------+--------------+
|  ident|          type|  municipality|
+-------+--------------+--------------+
|    5A8|MEDIUM_AIRPORT|     ALEKNAGIK|
|AF-0005|MEDIUM_AIRPORT|         KHOST|
|   AGGH|MEDIUM_AIRPORT|       HONIARA|
|    AHJ|MEDIUM_AIRPORT|           ABA|
|   ANYN|MEDIUM_AIRPORT|YAREN DISTRICT|
|AU-0121|MEDIUM_AIRPORT|        KILCOY|
|    AXF|MEDIUM_AIRPORT|      BAYANHOT|
|   AYBK|MEDIUM_AIRPORT|   BUKA ISLAND|
|   AYCH|MEDIUM_AIRPORT|      KUNDIAWA|
|   AYDU|MEDIUM_AIRPORT|          DARU|
|   AYGA|MEDIUM_AIRPORT|       GORONKA|
|   AYGN|MEDIUM_AIRPORT|        GURNEY|
|   AYGR|MEDIUM_AIRPORT|    POPONDETTA|
|   AYHK|MEDIUM_AIRPORT|       HOSKINS|
|   AYKM|MEDIUM_AIRPORT|        KEREMA|
|   AYKV|MEDIUM_AIRPORT|       KAVIENG|
|   AYMD|MEDIUM_AIRPORT|        MADANG|
|   AYMH|MEDIUM_AIRPORT|   MOUNT HAGEN|
|   AYMN|MEDIUM_AIRPORT|         MENDI|
|   AYMO|MEDIUM_AIRPORT|  MANUS ISLAND|
+-------+--------------+--------------+



flight_dataframe:
+------+-----------+----------+
|origin|destination|       day|
+------+-----------+----------+
|  KJFK|       KATL|2020-01-01|
|  KLAX|       YSSY|2020-01-01|
|  KLAX|       KPDX|2020-01-01|
|  KLAX|       YSSY|2020-01-01|
|  KLAX|       KBOS|2020-01-01|
|  KLAX|       KFAT|2020-01-01|
|  VHHH|       KBOS|2020-01-01|
|  RKSI|       KJFK|2020-01-01|
|  VHHH|       KJFK|2020-01-01|
|  EGLL|       KSFO|2020-01-01|
|  LSZH|       KSFO|2020-01-01|
|  ZGSZ|       KLAX|2020-01-01|
|  LSZH|       MROC|2020-01-01|
|  RPLL|       KJFK|2020-01-01|
|  WSSS|       KLAX|2020-01-01|
|  RPLL|       KSFO|2020-01-01|
|  KSEA|       RCTP|2020-01-01|
|  RPLL|       KLAX|2020-01-01|
|  LFPG|       KLAX|2020-01-01|
|  VHHH|       KLAX|2020-01-01|
+------+-----------+----------+
Total count: 887595

inter_city_flight_dataframe output:
+--------------------+------------+---------+----------+----------+             
|           from_city|from_airport|  to_city|to_airport|       day|
+--------------------+------------+---------+----------+----------+
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-15|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-17|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-21|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-21|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-25|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-26|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-02-29|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-05|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-07|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-11|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-12|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-15|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-15|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-18|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-19|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-20|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-20|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-21|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-23|
|WILKES-BARRE/SCRA...|        KAVP|CHARLOTTE|      KCLT|2020-03-24|
+--------------------+------------+---------+----------+----------+




city_from_and_to_flight_counts_dataframe on small_flight.csv dataset:
+-------------+----------+---------------------+---------------------+          
|         city|       day|incoming_flight_count|outgoing_flight_count|
+-------------+----------+---------------------+---------------------+
|NEW YORK CITY|2020-03-29|                    1|                    6|
|   WASHINGTON|2020-03-30|                    1|                    1|
|NEW YORK CITY|2020-03-30|                    1|                    1|
|SAN FRANCISCO|2020-03-30|                    5|                    4|
|NEW YORK CITY|2020-03-31|                    5|                   14|
|SAN FRANCISCO|2020-03-31|                    1|                    1|
|  LOS ANGELES|2020-03-31|                    1|                    1|
+-------------+----------+---------------------+---------------------+

Flight and Covid daily count on small_flight.csv:
+-------------+----------+-----+------+---------------------+---------------------+
|         city|       day|cases|deaths|incoming_flight_count|outgoing_flight_count|
+-------------+----------+-----+------+---------------------+---------------------+
|  LOS ANGELES|2020-03-31| 3011|    54|                    1|                    1|
|NEW YORK CITY|2020-03-29|33768|   776|                    1|                    6|
|NEW YORK CITY|2020-03-30|38087|   914|                    1|                    1|
|NEW YORK CITY|2020-03-31|43139|  1096|                    5|                   14|
|SAN FRANCISCO|2020-03-30|  374|     6|                    5|                    4|
|SAN FRANCISCO|2020-03-31|  400|     6|                    1|                    1|
|   WASHINGTON|2020-03-30|  401|     9|                    1|                    1|
+-------------+----------+-----+------+---------------------+---------------------+



city_from_and_to_flight_counts_dataframe on merged_flight.csv dataset:
+--------------+----------+---------------------+---------------------+         
|          city|       day|incoming_flight_count|outgoing_flight_count|
+--------------+----------+---------------------+---------------------+
|   LOS ANGELES|2020-01-01|                  516|                  543|
|       CHICAGO|2020-01-01|                  755|                  696|
|       HOUSTON|2020-01-01|                  395|                  374|
|  INDIANAPOLIS|2020-01-01|                  117|                  105|
|    WASHINGTON|2020-01-01|                  343|                  291|
|   SAN ANTONIO|2020-01-01|                   66|                   83|
|        BOSTON|2020-01-01|                  312|                  299|
|       SEATTLE|2020-01-01|                  370|                  380|
|        DALLAS|2020-01-01|                  140|                  127|
|        DENVER|2020-01-01|                  126|                  429|
|     NASHVILLE|2020-01-01|                  154|                  145|
|SALT LAKE CITY|2020-01-01|                   76|                   30|
|     SAN DIEGO|2020-01-01|                  204|                  203|
|  PHILADELPHIA|2020-01-01|                  227|                  220|
|       DETROIT|2020-01-01|                  252|                   23|
|      SAN JOSE|2020-01-01|                  183|                  181|
| SAN FRANCISCO|2020-01-01|                  381|                  367|
|       PHOENIX|2020-01-01|                  411|                  373|
|     CHARLOTTE|2020-01-01|                  130|                  328|
| NEW YORK CITY|2020-01-01|                  537|                  524|
+--------------+----------+---------------------+---------------------+

Total Count = 1782 rows

Flight and Covid daily count on merged_flight.csv:
+------+----------+-----+------+---------------------+---------------------+    
|  city|       day|cases|deaths|incoming_flight_count|outgoing_flight_count|
+------+----------+-----+------+---------------------+---------------------+
|BOSTON|2020-02-01|    1|     0|                  341|                  310|
|BOSTON|2020-02-02|    1|     0|                  299|                  293|
|BOSTON|2020-02-03|    1|     0|                  395|                  405|
|BOSTON|2020-02-04|    1|     0|                  423|                  424|
|BOSTON|2020-02-05|    1|     0|                  392|                  387|
|BOSTON|2020-02-06|    1|     0|                  378|                  378|
|BOSTON|2020-02-07|    1|     0|                  400|                  378|
|BOSTON|2020-02-08|    1|     0|                  364|                  332|
|BOSTON|2020-02-09|    1|     0|                  312|                  322|
|BOSTON|2020-02-10|    1|     0|                  404|                  406|
|BOSTON|2020-02-11|    1|     0|                  418|                  397|
|BOSTON|2020-02-12|    1|     0|                  415|                  399|
|BOSTON|2020-02-13|    1|     0|                  392|                  388|
|BOSTON|2020-02-14|    1|     0|                  450|                  421|
|BOSTON|2020-02-15|    1|     0|                  312|                  282|
|BOSTON|2020-02-16|    1|     0|                  326|                  335|
|BOSTON|2020-02-17|    1|     0|                  380|                  376|
|BOSTON|2020-02-18|    1|     0|                  403|                  410|
|BOSTON|2020-02-19|    1|     0|                  436|                  398|
|BOSTON|2020-02-20|    1|     0|                  432|                  407|
+------+----------+-----+------+---------------------+---------------------+
Total count = 782 rows

```

Next Steps:
1. Joining the datagrams to get the desired results
