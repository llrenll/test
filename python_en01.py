#lesson.csv

import csv
from os import name

with open('./python/lesson.csv','r', encoding='utf-8-sig') as csv_file:
    read = csv.DictReader(csv_file)
    sd = []

    for row in read:
        row['合計'] = int(row['国語']) + int(row['数学']) + int(row['社会'])
        print(list(row.values()))
        sd.append({'seq':row['seq'],'name':row['name'], '合計':row['合計']})


for i in sd:
    print(list(i.values()))


with open('./python/lesson02.csv', 'w', encoding='utf-8',newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['seq','name','合計'])
    for i in sd:
        writer.writerow(list(i.values()))
