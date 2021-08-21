# This program sorted the numbers below 20 in descending order
# create empty list to store numbers
list = []

# loop to get 10 integer numbers
for i in range(0, 10):
    # append each input into list
    list.append(int(input('Enter an integer number: ')))
# printing list
print(list)

# create another list to store sorted numbers
list2 = []

# loop to store number that are only less than 20
for i in list:
    # check condition if nmber is less than 20
    if i < 20:
        # if yes then print number and there type
        print(i, type(i))
        # and append it to list2
        list2.append(i)

# print list2
print(list2, type(list2), len(list2))

# loop to sort the numbers in descending order
for i in range(0, len(list2)-1):
    # internal to compare two numbers
    for j in range(i+1, len(list2)):
        # check if first number is less than second number
        if list2[i] < list2[j]:
            # if yes then interchange the numbers
            list2[i], list2[j] = list2[j], list2[i]
    # print iteration number
    print(i)
    # print final sorted list
    print(list2, type(list2), len(list2))
