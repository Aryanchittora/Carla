import csv
import json

csvData = []
names = ['throttle', 'steer', 'brake', 'hand_brake']

with open("data_set.txt", "r") as f:
    data = json.loads(f.read())

file = open("Project-227.csv", "w", newline='')
writer = csv.DictWriter(file, fieldnames=names)
writer.writeheader()
writer.writerows(data)

with open("Project-227.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        csvData.append(row)
        print(csvData)  