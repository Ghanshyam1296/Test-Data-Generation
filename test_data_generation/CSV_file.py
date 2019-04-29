from faker import Faker
import csv

fake=Faker()
print('Enter the number of student for whom you want to generate CSV file')
x = input()

with open('sample.txt','w') as wf:
      csv_writer=csv.writer(wf, delimiter='|')

      for i in range(0,int(x)):
            csv_writer.writerow([fake.name(),fake.email(),fake.country()])


            
      
      
      
      
      

      
      
      

                     
    

            
    
                     
