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
```

Next Steps:
1. Joining the datagrams to get the desired results
