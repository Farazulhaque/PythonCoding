import calendar

year = int(input("Enter a year: "))
# check for the year
while True:
    if year > 1753:
        try:
            month = int(input("Enter a month number: "))
            # display the calendar
            print(calendar.month(year, month))
            break
        except IndexError:
            print("Month must be between 1 and 12")
        except ValueError:
            print("Month must be in Integer")
    else:
        print("Please enter year from 1753 forward")
