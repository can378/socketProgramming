#선수와 경기 기록 조회할 방법
import csv
f=open('Baseball.csv','r',encoding='UTF-8')
rdr=csv.reader(f)

for line in rdr:
    print(line)
f.close()

with open('Baseball_Team.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
        
