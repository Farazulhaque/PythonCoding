places = []
key = []
value = []

with open('codebook.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        places.append(currentPlace)

for i in range(len(places)):
    key.append(places[i][0])
    value.append(places[i][-1])

res = {key[i]: value[i] for i in range(len(key))}

print("*** Letter to Code")
for i, j in res.items():
    print(i, " -> ", j)
print()

print("*** Original Message")
msg = open("message.txt", "r")
message = msg.read()
print(message)

print("\n*** Encrypted Message")
for i in range(len(message)):
    for j in range(len(key)):
        if message[i] == key[j]:
            ind = key.index(message[i])
            encrypted = message.replace(message[i], value[ind])
print(encrypted)
