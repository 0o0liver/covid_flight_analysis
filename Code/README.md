# construct.py to generate the desired dataset #

`disease.csv`: This datasets contains COVID-19 data for cities in [`city_list.csv`](https://github.com/shantanutrip/covid_flight_analysis/blob/master/Datasets/city_list.csv).
Dataset looks like:
```
+--------------------+-----------+------------+    
|     City|      Date|      Cases|      Deaths|
+--------------------+-----------+------------+
|Allegheny|2020-03-14|          1|           0|
|Allegheny|2020-03-15|          3|           0|
|Allegheny|2020-03-16|          5|           0|
|Allegheny|2020-03-17|         10|           0|
+--------------------+------------+-----------+
```

## How to run the script: ##
See detailed instruction [here](https://github.com/shantanutrip/covid_flight_analysis/tree/master/Datasets#diseasecsv)

# driver.py to generate the desired datasets #

### The driver.py helps in making the 2 clean datasets that will be used for further analysis. The resultant datasets are: ###

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

In case you are following the Long Process, to run the script, we need to go through the process of making initial datasets. The process is mentioned on https://github.com/shantanutrip/covid_flight_analysis/tree/master/Datasets. In case you are following the Short Process, you do not need to do this.

After we successfully get the initial data, we will have the following data on our hfs:
1. disease.csv
2. airports.csv
3. city_list.csv
4. map_list.csv
5. merged_flight.csv

Once we have the above files in hfs, we can run the script.

**The only script we will be running is driver.py.**

The **input** of the script will be the **5 initial datasets i.e. disease.csv, airports.csv, city_list.csv, map_list.csv and merged_flight.csv**.

The **output** of the script will be 2 dataset folders which will  be saved by the script on hfs. The datasets will be called **inter_city_flight_data.out** and **covid_flight_count_data.out**.

## We need to follow the given steps: ##

1. Clone the repository and upload https://github.com/shantanutrip/covid_flight_analysis/blob/master/Code/driver.py on your hpc VM. 

***Note, from step 2 onwards (including step 2), all the commands will be typed on the hpc VM.***

2. To begin with, let us remove any folders on hfs that have the same name as our resultant datasets: <br>
  a.```hfs -rm -r covid_flight_count_data.out```  <br>
  b.```hfs -rm -r inter_city_flight_data.out``` <br>

3. ```module load python/gnu/3.6.5``` <br>
4. ```module load spark/2.4.0``` <br>

5. The following command will take 5 to 10 minutes to run. This is because one of the input datasets is huge. Run this command in the directory where you have uploaded driver.py <br>

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

For eg., if all the above datasets exist in ```Datasets/``` folder on hfs, the command would look like: <br>

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

6.
Once the data is successfully made on hfs, we can get the merged file to our hpc VM using the following commands: <br>

```hfs -getmerge inter_city_flight_data.out data_intercity_with_multiple_headers.csv``` <br>

```hfs -getmerge covid_flight_count_data.out data_covid_with_multiple_headers.csv``` <br>

7. The files we have received have multiple headers and we want to get rid of them using the following commands: <br>

```awk 'BEGIN{f=""}{if($0!=f){print $0}if(NR==1){f=$0}}' data_intercity_with_multiple_headers.csv > inter_city_flight_data.csv```

```awk 'BEGIN{f=""}{if($0!=f){print $0}if(NR==1){f=$0}}' data_covid_with_multiple_headers.csv > covid_flight_count_data.csv```

8. We can remove the files with multiple headers: <br>

```rm data_covid_with_multiple_headers.csv``` <br>

```rm data_intercity_with_multiple_headers.csv``` <br>

9. **You have reached the end of the process. Your current directory in the hpc cluster has the following 2 resultant dataset files:** <br>

```inter_city_flight_data.csv``` <br>

```covid_flight_count_data.csv``` <br>

The resultant datasets are present in the following:
https://github.com/shantanutrip/covid_flight_analysis/tree/master/Resultant_Data <br>


```
inter_city_flight_data.csv (Total count: 887595 (+ 1 header))
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


covid_flight_count_data.csv (Total count: 782 (+ 1 header)):
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

```
