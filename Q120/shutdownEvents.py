# find specific line from text file that contains shutdown initiated
import re

# open file to read
with open("Q120\logfile.txt", "r") as file:
    # loop in each line
    for line in file:
        # search in each line
        if (re.search("Shutdown initiated", line)):
            # if found then print tht line
            print(line)

