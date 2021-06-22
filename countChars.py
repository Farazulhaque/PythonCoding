word = input("Enter String: ")


# count number of occurences
count = []

# Create list of uniques characters
newlist = []

for i in range(len(word)):
    # Checking for duplicate characters
    if word[i] not in newlist:
        newlist.append(word[i])
        x = word.count(word[i])
        count.append(x)


result = {}
print()
# Append key-value pair to a result dictionary
for i in range(len(newlist)):
    result[newlist[i]] = count[i]

print(result)
