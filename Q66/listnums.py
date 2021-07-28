# Create empty list to store numbers
l1 = []
# loop untill the list contain 10 numbers
while len(l1) < 10:
    # get user input
    num = int(input("Enter number: "))
    # check for number is already in list or not
    if num not in l1:
        # add number to the list
        l1.append(num)

# Print contents of the list
print(l1)
# Print sum of numbers in a list
print(f"Sum: {sum(l1)}")
# Print average of numbers in a list
print(f"Average: {sum(l1)/len(l1)}")


