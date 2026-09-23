import csv

APP = "Instagram"
minutes = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))

minutes = minutes[0:7]

total = sum(minutes)
average = total // len(minutes)
highest = max(minutes)
lowest = min(minutes)

count = 0

for value in minutes:
    if value > average:
        count += 1

print(f"Name: {APP}, Total_Minutes: {total}, Average_Minutes: {average}, Highest_Minutes: {highest}, Lowest_Minutes: {lowest}, Days_Above_Average: {count}")