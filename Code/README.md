# Initial Data Processing For Airport, Flight and Covid Dataset #

**Currently the script is called rough_commands.py** 
**It runs fine. The name will be changed later**

To run the script, we need to have the following data in the hpc:
1. Datasets/us-counties.csv 
2. Datasets/merged_flight.csv
3. Datasets/airports.csv
4. Datasets/map_list.csv
5. Datasets/city_list.csv

Once we have the above files in hpc, we can run the script.

The script:
1. Cleans the dataset
2. Standardises the dataset. Removes leading and trailing spaces and converts the entire data into upper case.
2. Maps the city names to the desired names using map_list.csv
3. Filters the cities specified by the user in city_list.csv
4. Currnetly, gives us the following datagrams at the end.

```
covid_dataframe:
+----------+--------------+-----+------+
|      date|        county|cases|deaths|
+----------+--------------+-----+------+
|2020-03-01|       PHOENIX|    1|     0|
|2020-03-01|   LOS ANGELES|    1|     0|
|2020-03-01|     SAN DIEGO|    1|     0|
|2020-03-01| SAN FRANCISCO|    3|     0|
|2020-03-01|      SAN JOSE|    7|     0|
|2020-03-01|       CHICAGO|    3|     0|
|2020-03-01|        BOSTON|    1|     0|
|2020-03-01| NEW YORK CITY|    1|     0|
|2020-03-01|    WASHINGTON|    2|     0|
|2020-03-01|   SAN ANTONIO|   11|     0|
|2020-03-01|SALT LAKE CITY|    1|     0|
|2020-03-01|       SEATTLE|   11|     3|
|2020-03-02|       PHOENIX|    1|     0|
|2020-03-02|   LOS ANGELES|    1|     0|
|2020-03-02|     SAN DIEGO|    1|     0|
|2020-03-02| SAN FRANCISCO|    3|     0|
|2020-03-02|      SAN JOSE|    9|     0|
|2020-03-02|       CHICAGO|    4|     0|
|2020-03-02|        BOSTON|    1|     0|
|2020-03-02| NEW YORK CITY|    1|     0|
+----------+--------------+-----+------+

airport_dataframe:
+-----+--------------+--------------+--------+
|ident|          type|  municipality|gst_code|
+-----+--------------+--------------+--------+
|  5A8|MEDIUM_AIRPORT|     ALEKNAGIK|     5A8|
| AGGH|MEDIUM_AIRPORT|       HONIARA|    AGGH|
|  AHJ|MEDIUM_AIRPORT|           ABA|    ZUHY|
| ANYN|MEDIUM_AIRPORT|YAREN DISTRICT|    ANYN|
|  AXF|MEDIUM_AIRPORT|      BAYANHOT|    ZBAL|
| AYBK|MEDIUM_AIRPORT|   BUKA ISLAND|    AYBK|
| AYCH|MEDIUM_AIRPORT|      KUNDIAWA|    AYCH|
| AYDU|MEDIUM_AIRPORT|          DARU|    AYDU|
| AYGA|MEDIUM_AIRPORT|       GORONKA|    AYGA|
| AYGN|MEDIUM_AIRPORT|        GURNEY|    AYGN|
| AYGR|MEDIUM_AIRPORT|    POPONDETTA|    AYGR|
| AYHK|MEDIUM_AIRPORT|       HOSKINS|    AYHK|
| AYKM|MEDIUM_AIRPORT|        KEREMA|    AYKM|
| AYKV|MEDIUM_AIRPORT|       KAVIENG|    AYKV|
| AYMD|MEDIUM_AIRPORT|        MADANG|    AYMD|
| AYMH|MEDIUM_AIRPORT|   MOUNT HAGEN|    AYMH|
| AYMN|MEDIUM_AIRPORT|         MENDI|    AYMN|
| AYMO|MEDIUM_AIRPORT|  MANUS ISLAND|    AYMO|
| AYNZ|MEDIUM_AIRPORT|           LAE|    AYNZ|
| AYPY| LARGE_AIRPORT|  PORT MORESBY|    AYPY|
+-----+--------------+--------------+--------+



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

inter_city_flight_dataframe output:
+--------------------+------------+-------------+----------+----------+         
|           from_city|from_airport|      to_city|to_airport|       day|
+--------------------+------------+-------------+----------+----------+
|              LONDON|        EGLL|NEW YORK CITY|      KJFK|2020-03-31|
|              LONDON|        EGLL|SAN FRANCISCO|      KSFO|2020-03-30|
|FAYETTEVILLE/SPRI...|        KXNA|NEW YORK CITY|      KLGA|2020-03-31|
|          WASHINGTON|        KIAD|SAN FRANCISCO|      KSFO|2020-03-30|
|          FORT MYERS|        KRSW|NEW YORK CITY|      KLGA|2020-03-29|
|             MADISON|        KMSN|SAN FRANCISCO|      KSFO|2020-03-30|
|       NEW YORK CITY|        KJFK|    SAN DIEGO|      KSAN|2020-03-31|
|       NEW YORK CITY|        KJFK|        TOKYO|      RJTT|2020-03-31|
|       NEW YORK CITY|        KJFK|        SEOUL|      RKSI|2020-03-31|
|       NEW YORK CITY|        KJFK|  LOS ANGELES|      KLAX|2020-03-31|
|       NEW YORK CITY|        KJFK|      PHOENIX|      KPHX|2020-03-31|
|       NEW YORK CITY|        KJFK|SAN FRANCISCO|      KSFO|2020-03-31|
|       NEW YORK CITY|        KJFK|SAN FRANCISCO|      KSFO|2020-03-30|
|              NEWARK|        KEWR|SAN FRANCISCO|      KSFO|2020-03-30|
|       NEW YORK CITY|        KLGA|    CLEVELAND|      KCLE|2020-03-29|
|       NEW YORK CITY|        KLGA|  KANSAS CITY|      KMCI|2020-03-31|
|       NEW YORK CITY|        KLGA|      DETROIT|      KDTW|2020-03-29|
|       NEW YORK CITY|        KLGA|     ST LOUIS|      KSTL|2020-03-31|
|       NEW YORK CITY|        KLGA|    KNOXVILLE|      KTYS|2020-03-31|
|       NEW YORK CITY|        KLGA|  MINNEAPOLIS|      KMSP|2020-03-29|
+--------------------+------------+-------------+----------+----------+




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

city_from_and_to_flight_counts_dataframe on merged_flight.csv dataset:
+--------------+----------+---------------------+---------------------+         
|          city|       day|incoming_flight_count|outgoing_flight_count|
+--------------+----------+---------------------+---------------------+
|   LOS ANGELES|2020-01-01|                  516|                  543|
|       CHICAGO|2020-01-01|                  755|                  696|
|       SEATTLE|2020-01-01|                  370|                  380|
|  INDIANAPOLIS|2020-01-01|                  117|                  105|
|     SAN DIEGO|2020-01-01|                  204|                  203|
|   SAN ANTONIO|2020-01-01|                   66|                   83|
|       DETROIT|2020-01-01|                  252|                   23|
|        BOSTON|2020-01-01|                  312|                  299|
|       HOUSTON|2020-01-01|                  395|                  374|
|        DALLAS|2020-01-01|                  140|                  127|
|        DENVER|2020-01-01|                  126|                  429|
|    WASHINGTON|2020-01-01|                  343|                  291|
|     NASHVILLE|2020-01-01|                  154|                  145|
|  PHILADELPHIA|2020-01-01|                  227|                  220|
|SALT LAKE CITY|2020-01-01|                   76|                   30|
|      SAN JOSE|2020-01-01|                  183|                  181|
|       PHOENIX|2020-01-01|                  411|                  373|
| SAN FRANCISCO|2020-01-01|                  381|                  367|
|     CHARLOTTE|2020-01-01|                  130|                  328|
| NEW YORK CITY|2020-01-01|                  537|                  524|
+--------------+----------+---------------------+---------------------+

Total Count = 1782 rows

```

Next Steps:
1. Joining the datagrams to get the desired results
