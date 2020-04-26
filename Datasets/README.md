# Explanation and Generation of datasets
## disease.csv:
This dataset contains four columns: *city*, *date*, *cases* and *deaths* and you can find this dataset from [here](https://github.com/shantanutrip/covid_flight_analysis/tree/master/Disease_data) <br>
* City: In order to make more precise analysis, we need to find the cities with large populations and big amounts of flights per day. So, we chose these cities from the top 25 largest cities around the US. City list can be found inside ```city_list.txt``` where each line represents “*city*, *state*”.
* Date: Given the very first case of the US appears in January and only less than 10 cities have the first case before March, so we will mainly consider the epidemic situation for March and April. However, the generated dataset still includes lines of data for January and February.
* Cases: This represents the cumulative infected number for considered cities day by day. 
* Deaths: This represents the cumulative death number for considered cities day by day.

To get this file from raw data, we use the data source from an [authoritative webpage](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv) <br>
Here is some instructions to output one csv file we want:
1. Under the same folder named “*Disease_data*”, download every file.
2. Run "*construct.py*" by ```python construct.py 'str'```, where ```str``` can be replaced by the months you are interested in. If you want every month from the beginning of the spread of the epidemic, ```str``` should be ```01,02,03,04```; while ```03``` for only March.
3. Then, there will be a csv file outputted. Four columns are ordered by city and date.

Supplementary instructions:
1. When we extract data from the source data webpage, the reason for considering both city and state is some cities appear in more than one state. So, we want the program to know the real city we want.
2. Some cities are not exactly what we know before, for example: Cook should be Chicago, Suffolk should be Boston. This issue results from the format of the data source, where they collect data in terms of county rather than city. To fix this, users can find the mapping relationship for city and county inside README.
3. If you want to add more cities into city_list.csv, please follow the same format and look up for the county that the city is inside.


## merged_flight.csv
This dataset contains information of every flight during the first three months of 2020. This dataset is generated from data that was provided by [Opensky Network](https://opensky-network.org/), source files can be found [here](https://opensky-network.org/datasets/covid-19/). There are 10 columns in this dataset, however, we only utilized 3 of the 10, they are *origin*, *destination* and *day*. 
* Origin: ICAO 4-characters code of the origin airport.
* Destination: ICAO 4-characters code of the destination airport.
* Day: Date of each flight.

Due to the large size of this file, we are not able to upload it to this repo, therefore, instructions on how to generate ```merged_flight.csv``` is provided below:
1. Download file ```flight_dataset_urls.txt``` from the repo and place it to the desired directory in the HPC vm.
2. Run command ```cat flight_dataset_urls.txt | xargs -n 1 -P 8 wget -c -P flight/``` to download three individual zipped dataset files to the flight directory.
3. Navigate to flight directory using ```cd flight```.
4. Run command ```gunzip *.gz``` to unzip three individual dataset files.
5. Navigate back to the previous directory using ```cd ..```.
6. Run command ```hfs -put flight``` to upload flight directory to the distributed file system.
7. Run command ```hfs -getmerge flight flight.csv``` to merge three individual dataset files to one file and download it (```flight.csv``` will have two extra header lines because ```-getmerge``` command performs plain concatenation of files, step 8 takes care of this issue).
8. Run command ```awk 'BEGIN{f=""}{if($0!=f){print $0}if(NR==1){f=$0}}' flight.csv > merged_flight.csv``` to get rid of the two extra header lines

## airports.csv
This dataset contains information of every airport in the world, this dataset is provided by [OurAirports](https://ourairports.com/) and can be downloaded [here](https://ourairports.com/data/airports.csv). This dataset has 18 columns of information for each airport, we only utilized 4 of the 18, they are *ident*, *type*, *name* and *municipality*.
* Ident: ICAO 4-characters code of airports
* Type: Type of airports, for the scope of this project, we only care about “large_airport” and “medium_airport”.
* Name: Name of airports
* Municipality: Name of the city that each airport is located. 

