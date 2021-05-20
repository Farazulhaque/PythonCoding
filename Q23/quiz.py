import random

places = []
key = []
value = []

filename = input("What is the name of the question file? ")
with open(filename, 'r') as filehandle:
    for line in filehandle:
        places.append(line.strip('\n'))

for i in range(len(places)):
    items = places[i].split(",")
    key.append(items[0])
    value.append(items[1])

count = 0
for i in range(3):
    question = random.choice(key)
    que = input(question)
    ind = key.index(question)
    if value[ind] == que:
        print("Correct!")
        count += 1
    else:
        print("Incorrect!  The answer is ", value[ind])

print("You got " + str(count) +
      " answers correct out of 3, which is " + str(count*100/3) + "%")
