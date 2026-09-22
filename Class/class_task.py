APP = "Instagram"

minutes = [95, 120, 80, 140, 60, 170, 110]

total = 0
for value in minutes:
    total += value

average = total / len(minutes)

highest = minutes[0]
for value in minutes:
    if value > highest:
        highest = value

lowest = minutes[0]
for value in minutes:
    if value < lowest:
        lowest = value

count = 0
for value in minutes:
    if value > average:
        count += 1

print("App:", APP)
print("Total Minutes:", total)
print("Average Minutes:", average)
print("Highest Minutes:", highest)
print("Lowest Minutes:", lowest)
print("Days Above Average:", count)