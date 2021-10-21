def main():
    # getting user input name of file
    fileName = input(
        "Please enter the name of the file with names and grades in it: ")

    # call function processFile to process it
    processFile(fileName)


def processFile(fileName):
    # open file in read only mode
    inFile = open(fileName, "r")
    # print header
    print("{0:10} {1:10} {2:8} {3:8} {4:5}".format(
        "Last Name", "First Name", "# scores", "Average", "Grade"))

    # loop until end of file line by line
    for line in inFile:
        # split the each line separated by comma
        information = line.split(",")
        # assign values
        lName = information[0]
        fName = information[1]
        grade = information[2:]
        # to remember total and count
        total = 0
        count = 0
        # to calculate total and count
        for x in grade:
            total += int(x)
            count += 1
        # calculate average
        average = total/count
        letter = ""
        # get grade of student
        if (average >= 94):
            letter = "A"
        elif (average >= 90):
            letter = "A-"
        elif (average >= 87):
            letter = "B+"
        elif (average >= 84):
            letter = "B"
        elif (average >= 80):
            letter = "B-"
        elif (average >= 77):
            letter = "C+"
        elif (average >= 74):
            letter = "C"
        elif (average >= 70):
            letter = "C-"
        elif (average >= 67):
            letter = "D+"
        elif (average >= 64):
            letter = "D"
        elif (average >= 60):
            letter = "D-"
        else:
            letter = "E"
        # printdetails of each student
        print("{0:10} {1:10} {2:5} {3:10.2f} {4:10}".format(
            lName, fName, count, average, letter))

    # close the file
    inFile.close()


# calling main
main()
