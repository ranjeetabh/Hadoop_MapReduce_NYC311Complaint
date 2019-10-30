# Hadoop_MapReduce_NYC311Complaint

This directory consists of the following files:

1) complaint_count.py: Python map reduce script to calculate aggregate count of specific complaint types.
2) average_count.py: Python map reduce script to calculate average of each complaint type per quarter FY 2017.
3) illegal_parking_count.py: Python map reduce script to determine the borough having maximum number of illegal parking.
4) HW2_Cloud_Computing: Relevant document of the project.
5) Sample .mrjob.conf file: Sample configuration file for running job in Amazon EC2 hadoop cluster.



This project aims to process NYC 311 Complaints data and answer some insightful questions from the same. Hadoop MapReduce software framework is used to read and extract information from the input file. Python scripts are executed in Amazon EC2 hadoop cluster. Input file sized 5.9GB can be accessed from (https://pgarias-bucket-cloud.s3.us-east-2.amazonaws.com/311_Service_Requests_from_2015_to_Present.csv). Sample extract of 1000 records can be accessed from (https://pgarias-bucket-cloud.s3.us-east-2.amazonaws.com/311_Service_Requests_from_2015_to_Present_head_1000.csv). The following details are extracted from the file post processing:

1) Number of open, assigned and closed issues for the following 3 complaint types: 
  - Noise
  - Street Condition
  - Illegal Parking
  
Answer: 	    

- "Count of Noise_Complaints":  			1771120
- "Count of Illegal Parking Complaints":		561212
- "Count of Street Condition Complaints":		434132
        
2) For the year 2017, for each quarter (Jan-Mar, April-June, July-Sept, Oct-Dec):

Answer: Average number of the above complaints per month 

- "Average number of noise complaints per month in Q1 (Jan - Mar)":	 		27964
- "Average number of street complaints per month in Q1 (Jan - Mar)":			8581
- "Average number of illegal parking complaints per month in Q1 (Jan - Mar)":		10772
- "Average number of noise complaints per month in Q2 (Apr - June)":			43789
- "Average number of street complaints per month in Q2 (Apr - June)":			10704
- "Average number of illegal parking complaints per month in Q2 (Apr - June)":		12971
- "Average number of noise complaints per month in Q3 (July - Sept)":			43990
- "Average number of street complaints per month in Q3 (July - Sept)":			6590
- "Average number of illegal parking complaints per month in Q3 (July - Sept)":		12784
- "Average number of noise complaints per month in Q4 (Oct - Dec)":			33286
- "Average number of street complaints per month in Q4 (Oct - Dec)":			5212
- "Average number of illegal parking complaints per month in Q4 (Oct - Dec)"	:	12179

3) For the year 2017, for each quarter (Jan-Mar, April-June, July-Sept, Oct-Dec):

Answer:Borough with the highest number of illegal parking each quarter
  
 
- "Highest number of illegal parking borough in Q1 (Jan-Mar)":		["BROOKLYN"]
- "Highest number of illegal parking borough in Q2 (Apr-June)":		["BROOKLYN"]
- "Highest number of illegal parking borough in Q3 (July-Sept)":	["BROOKLYN"]
- "Highest number of illegal parking borough in Q4 (Oct-Dec)":		["BROOKLYN"]

