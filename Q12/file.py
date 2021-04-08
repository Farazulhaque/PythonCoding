import sys
filename = input("Enter name of the file that contain numbers: ")
sum = 0
try:
    with open(filename) as input_data:
        # Using accumulator pattern to get the number stored in each line
        for each_line in input_data:
            try:
                number = float(each_line.strip())
                print(number)
                sum += number

            # the except block will except the line which in which there is no number
            # i.e if it contain string , the it is excepted
            except ValueError as e:
                print('Warning: Unable to parse %s: %s' % (each_line, e))

        # it will print the total of the numbers
        print("The total of the numbers in {} is {}".format(filename, sum))

# this except block will except if something is wrong with filename e.g file not available
except EnvironmentError as err_open:
    print('Error accessing file %s: %s' % (filename, err_open))
