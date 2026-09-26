import numpy as np
import csv

insta_minutes = []
study_minutes = []

with open("./digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row["Instagram_Minutes"]))
        study_minutes.append(int(row["Study_Minutes"]))

insta_minutes = insta_minutes[:7]
study_minutes = study_minutes[:7]

Instagram = np.array(insta_minutes)
Study = np.array(study_minutes)

print(Instagram, Study)

total = Instagram.sum()
average = Instagram.mean()
maximum = Instagram.max()
minimum = Instagram.min()
days = len(Instagram)

print(f"""Total: {total},
Average: {average},
Maximum: {maximum},
Minimum: {minimum},
Days: {days}""")

print(Instagram[0], Instagram[-1], Instagram[2])
print(Instagram[:3], Instagram[-2:], Instagram[1:4], Instagram[::2])

I_hours = (Instagram / 60).round(2)
print(I_hours)

s_total = Study.sum()
s_average = Study.mean()
s_maximum = Study.max()
s_minimum = Study.min()
s_days = len(Study)

print(f"""Total: {s_total},
Average: {s_average},
Maximum: {s_maximum},
Minimum: {s_minimum},
Days: {s_days}""")

print(Study[0], Study[-1], Study[2])
print(Study[:3], Study[-2:], Study[1:4], Study[::2])

S_hours = (Study / 60).round(2)
print(S_hours)

difference = Study - Instagram
print(difference)

greater = Instagram[Instagram > 100]
print(greater)

count = (Instagram > 100).sum()
print(count)

above_average = Instagram[Instagram > average]
print(above_average)
