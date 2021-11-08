# find number from text file and return the sum of total numbers

import re
# create a text variable to store file content
text = ""

# open file to read
with open("Q115\sample_file.txt", "r") as file:
    # loop in each line
    for line in file:
        # store each line int text variable
        text += line


# store the output of re.findall() into numbers variable
# it will extract all the numbers from the text
# because of regular expression [0-9]+
# and return list of numbers as output
numbers = re.findall("[0-9]+", text)
print(numbers)
# to find sum, set initial value to 0
sum = 0
# loop in list of numbers
for num in numbers:
    # convert each value to int and add to sum
    sum += int(num)

# print sum of numbers
print(sum)
