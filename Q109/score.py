import csv
from os import name

names = []
scores = []

with open("MIS6382 Fall2021-HW3Q2IIinput.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        st_name = row[0].strip()
        st_score = int(row[1])
        names.append(st_name.rstrip())
        scores.append(st_score)

# print(names)
# print(scores)

print("Enter the list of students who play basketball. Separate the names with ',': ")
basketballList = input().split(", ")
# print(basketballList)

print("\nEnter the list of students who play volleyball. Separate the names with ',': ")
volleyballList = input().split(", ")
# print(volleyballList)


onlybasketball = []
onlyVolleyball = []
bothGames = []
neitherGames = []
for name in basketballList:
    if name not in volleyballList:
        onlybasketball.append(name)
    else:
        bothGames.append(name)
for name in volleyballList:
    if name not in basketballList:
        onlyVolleyball.append(name)


for name in names:
    if name not in volleyballList and name not in basketballList:
        neitherGames.append(name)

print(f"\nStudent who play only Basketball {onlybasketball}")
print(f"\nStudent who play only Volleyball {onlyVolleyball}")
print(f"\nStudent who play both games {bothGames}")
print(f"\nStudent who neither games {neitherGames}")


for i in range(len(names)):
    if names[i] in onlyVolleyball:
        scores[i] += 5
    if names[i] in onlybasketball:
        scores[i] += 8
    if names[i] in bothGames and scores[i] >= 80:
        scores[i] += 10
    if names[i] in bothGames and scores[i] < 80:
        scores[i] -= 5
    if scores[i] > 100:
        scores[i] = 100

print("\nThe names of all students along with their adjusted scores is: ")
for i in range(len(names)):
    print("%-15s:%20d" % (names[i], scores[i]))
