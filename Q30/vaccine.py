# Creating empty list to append data
all = []
new = []

# variable loop condition
again = 'y'

# Initially again = 'y' to start the program
while again == 'y':
    # Printing menu
    print('\n(1) New Appointment: \n(2) Change Date: \n(3) Vaccinated: ')

    # getting user input
    ser = input('What service do you need: ')

    # if user inputted 1 i.e New Appointment
    if ser == '1':
        # Getting data Id, Name, and Date
        # Using split() to split the date by a space
        # And added in list new
        new = input("Enter ID Name Date: ").split()
        print('Added data =', new)

        # Now append the new list in all list
        all.append(new)
        print('All data =', all)

    # if user inputted 2 i.e Change Date
    elif ser == '2':
        # Getting ID of a person who want to change date
        IDchangeDate = input('ID person who wants to change: ')
        d = -1

        # this loop is used to check the ID is already available in all or not
        for i in range(len(all)):
            # If ID is already availabe
            if IDchangeDate == all[i][0]:
                # Then get New date
                newDate = input('New date: ')
                # And change the value of previous date to new date
                all[i][2] = newDate
                # and change value of d
                d = i
                print('All data =', all)
                break
        # If ID is not availabe in all then the value of d is not changed
        # So Cannot find Id
        if d == -1:
            print('Cannot find ID:', IDchangeDate)

    # if user inputted 3 i.e Vaccinated
    else:
        # Getting ID of person who gets vaccinated
        vaccinated = input('ID person who was vaccinated: ')
        d = -1

        # Again loop to check the ID is already available in all or not
        for i in range(len(all)):
            for j in range(len(all[i])):
                # If ID available then change value of d
                if vaccinated == all[i][j]:
                    d = i
                    break

        # If ID is not availabe then value of d is not changed
        # So, cannot find ID
        if d == -1:
            print('Cannot find ID:', vaccinated)

        # Else delete the all[d]
        else:
            del all[d]
            print('All data =', all)

    # Input to loop
    again = input('Do you want to continue? y(Yes), n(No) ')
