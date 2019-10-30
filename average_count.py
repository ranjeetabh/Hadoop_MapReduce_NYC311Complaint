## This script attempts to find the average number of different complaint types for each quarter for a given year

from mrjob.job import MRJob
from datetime import datetime

class MR311ServiceRequests(MRJob):
    
    def mapper(self, _, line):               
        q1_noise = 0                       ## Initialize Variables
        q1_parking = 0
        q1_street = 0
        q2_noise = 0
        q2_parking = 0
        q2_street = 0
        q3_noise = 0
        q3_parking = 0
        q3_street = 0
        q4_noise = 0
        q4_parking = 0
        q4_street = 0
 
        
        attr_list = line.split(",")       ## Splitting each line of the file  
        
        formatted_time = datetime
        
        if attr_list[1] !=  "Created Date":                    ## Formatting created date attribute
            attr_list[1] = attr_list[1][:-2].strip()
            formatted_time = datetime.strptime(attr_list[1], "%m/%d/%Y %H:%M:%S")
        else:
            pass
         
        
        if (formatted_time.year == 2017):                     ## Checking year
            if (formatted_time.month == 1) or (formatted_time.month == 2) or (formatted_time.month == 3): 
                if 'Noise' in attr_list[5]:                   
                    q1_noise += 1
                elif 'Illegal Parking' in attr_list[5]:
                    q1_parking += 1

                elif 'Street Condition' in attr_list[5]:
                    q1_street += 1
                    
            elif (formatted_time.month == 4) or (formatted_time.month == 5) or (formatted_time.month == 6): 
                if 'Noise' in attr_list[5]:
                    q2_noise += 1
                elif 'Illegal Parking' in attr_list[5]:
                    q2_parking += 1

                elif 'Street Condition' in attr_list[5]:
                    q2_street += 1
                    
            elif (formatted_time.month == 7) or (formatted_time.month == 8) or (formatted_time.month == 9): 
                if 'Noise' in attr_list[5]:
                    q3_noise += 1
                elif 'Illegal Parking' in attr_list[5]:
                    q3_parking += 1

                elif 'Street Condition' in attr_list[5]:
                    q3_street += 1
             
            elif (formatted_time.month == 10) or (formatted_time.month == 11) or (formatted_time.month == 12): 
                if 'Noise' in attr_list[5]:
                    q4_noise += 1
                elif 'Illegal Parking' in attr_list[5]:
                    q4_parking += 1
                elif 'Street Condition' in attr_list[5]:
                    q4_street += 1
                    
            else:
                pass
                                      
        else:
            pass
         
        yield "Average number of noise complaints per month in Q1 (Jan - Mar)", q1_noise
        yield "Average number of illegal parking complaints per month in Q1 (Jan - Mar)", q1_parking
        yield "Average number of street complaints per month in Q1 (Jan - Mar)", q1_street
        
        yield "Average number of noise complaints per month in Q2 (Apr - June)", q2_noise
        yield "Average number of illegal parking complaints per month in Q2 (Apr - June)", q2_parking
        yield "Average number of street complaints per month in Q2 (Apr - June)", q2_street
        
        yield "Average number of noise complaints per month in Q3 (July - Sept)", q3_noise
        yield "Average number of illegal parking complaints per month in Q3 (July - Sept)", q3_parking
        yield "Average number of street complaints per month in Q3 (July - Sept)", q3_street
        
        yield "Average number of noise complaints per month in Q4 (Oct - Dec)", q4_noise
        yield "Average number of illegal parking complaints per month in Q4 (Oct - Dec)", q4_parking
        yield "Average number of street complaints per month in Q4 (Oct - Dec)", q4_street
        
        
    def reducer(self, key, values):         
        yield key, round(sum(values)/3)          ## Finding average per month
    
              

if __name__ == '__main__':
    MR311ServiceRequests.run()
    
    