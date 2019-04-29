import csv

with open('sample.txt', 'r') as rf:
      csv_reader=csv.reader(rf,delimiter='|')

      with open('new_sample.txt','w') as wf:
            csv_writer=csv.writer(wf)

            for line in csv_reader:
                csv_writer.writerow(line)
                  
