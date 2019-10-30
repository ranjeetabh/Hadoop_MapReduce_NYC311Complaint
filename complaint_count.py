## This script attempts to find the number of open, assigned and closed issues for the following 3 complaint types:
## 1. All noise complaints
## 2. Street Condition
## 3. Illegal Parking

from mrjob.job import MRJob

class MR311ComplaintCount(MRJob):          
    
    def mapper(self, _, line):   
        attr_list = line.split(",")       
         
        count_noise_complaints = 0           ## Initialize Variables
        count_street_complaints = 0
        count_parking_complaints = 0     
        
        if (attr_list[0] == "Unique Key" or attr_list[1] == "Created Date"):   ## Ignore file header
            pass
        elif 'Noise' in attr_list[5]:                   ## Checking complaint type
            count_noise_complaints += 1
        elif 'Street Condition' in attr_list[5]:
            count_street_complaints += 1
        elif 'Illegal Parking' in attr_list[5]:
            count_parking_complaints += 1
        else:
            pass  
                         
        yield "Count of Noise_Complaints", count_noise_complaints
        yield "Count of Street Condition Complaints", count_street_complaints
        yield "Count of Illegal Parking Complaints", count_parking_complaints
        
   
        
    def reducer(self, key, values):          
        yield key, sum(values)
        
        
if __name__ == '__main__':
    MR311ComplaintCount.run()
    
    
