import csv
with open('HackOhio22-main/Dorm Buildings.csv', newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i in range(1):
        print(', '.join(data))   
