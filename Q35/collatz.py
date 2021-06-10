# This loop is to check input validation
loop = True
while loop == True:
    # This try block will execute if the input is number and positive number
    try:
        # get user input
        number = int(input("Enter a positive number: "))
        # check for positive number
        if number > 0:
            # Set loop to False as it is positive number
            loop = False
            # Initialise another loop for printing the number
            # and counting the no. of transformation
            innerLoop = True
            # initialise count as 0
            count = 0
            while innerLoop == True:
                # print the number and at the end attach "->" this
                print(int(number), end="->")
                # Check the condition
                if number % 2 == 0:
                    number = number / 2
                else:
                    number = (number * 3) + 1
                # Increment the count variable to 1
                count += 1
                if number == 1:
                    print(int(number))
                    print(count, "transformations")
                    # Since the number is equal to 1, we have to break the loop by
                    # giving innerLoop = False
                    innerLoop = False
        # If number is negative then this block will execute and continue the loop
        else:
            print("Please enter an integer value greater than zero\n")
    # This except block will execute if the input is not a number and continue the loop
    except ValueError:
        print("Please enter an integer value greater than zero\n")
