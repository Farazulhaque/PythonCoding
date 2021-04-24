# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst)
# sort list in decreasing order
lst.sort(reverse=True)

# count number of occurences
count = []

# Create list of uniques numbers
newlist = []

for i in range(len(lst)):
    if lst[i] not in newlist:
        newlist.append(lst[i])
        x = lst.count(lst[i])
        count.append(x)


newlist.sort(reverse=True)

print()
print("Value \t Count")
for i in range(len(newlist)):
    print(str(newlist[i]), " \t ", str(count[i]))
