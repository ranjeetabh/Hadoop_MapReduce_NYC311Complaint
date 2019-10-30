## This script attempts to find the number borough with the highest number of illegal parking each quarter for a given year

from mrjob.job import MRJob
from datetime import datetime

class MR311ServiceRequests(MRJob):
    
    def mapper(self, _, line):                
        q1_parking_borough = []            ## Initializing empty lists for holding parking borough names
        q2_parking_borough = []
        q3_parking_borough = []
        q4_parking_borough = []
        
        attr_list = line.split(",")       ## Splitting each line of the input file      
        
        formatted_time = datetime
        
        if attr_list[1] !=  "Created Date":                    ## Formatting created date attribute
            attr_list[1] = attr_list[1][:-2].strip()
            formatted_time = datetime.strptime(attr_list[1], "%m/%d/%Y %H:%M:%S")
        else:
            pass
        
         
        if (formatted_time.year == 2017):                     ## Checking year
            if (formatted_time.month == 1) or (formatted_time.month == 2) or (formatted_time.month == 3): 
                if 'Illegal Parking' in attr_list[5]:          ## Checking Parking Borough
                    q1_parking_borough.append(attr_list[30])
                    
            elif (formatted_time.month == 4) or (formatted_time.month == 5) or (formatted_time.month == 6): 
                if 'Illegal Parking' in attr_list[5]:
                    q2_parking_borough.append(attr_list[30])
                    
            elif (formatted_time.month == 7) or (formatted_time.month == 8) or (formatted_time.month == 9): 
                if 'Illegal Parking' in attr_list[5]:
                    q3_parking_borough.append(attr_list[30])
              
            elif (formatted_time.month == 10) or (formatted_time.month == 11) or (formatted_time.month == 12): 
                if 'Illegal Parking' in attr_list[5]:
                    q4_parking_borough.append(attr_list[30])    
            else:
                pass
                                      
        else:
            pass
       
        yield("Highest number of illegal parking borough in Q1 (Jan-Mar)",q1_parking_borough)
        yield("Highest number of illegal parking borough in Q2 (Apr-June)",q2_parking_borough)
        yield("Highest number of illegal parking borough in Q3 (July-Sept)",q3_parking_borough)
        yield("Highest number of illegal parking borough in Q4 (Oct-Dec)",q4_parking_borough)
            
      
    def reducer(self, key, values): 
        try:
            values = [x for x in values if x]                         ## Checking for empty values the list and removing them
            yield key, max(values, key=values.count)                  ## Picking most frequent value in the list
        except ValueError:                                            ## Compatible code for Python 2.7
            values = ["None"]
            yield key, values 
            
            #yield key, max(values, key=values.count, default = "None")  
            
        

if __name__ == '__main__':
    MR311ServiceRequests.run()
    
    
