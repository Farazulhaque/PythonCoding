monthDays = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31,
             'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
print(monthDays)

# getting user input
month = input("Enter 3 character abbreviation for month: ")
day = int(input("Enter day: "))
year = int(input("Enter year: "))


# checking month
def monthValidation(month):
    if month in monthDays.keys():
        return True
    else:
        return False


# checking day
def dayValidation(day):
    if day <= monthDays.get(month):
        return True
    else:
        return False


# checking year
def yearValidation(year):
    if year > 1752:
        # checking leap year
        if checkLeapYear(year) == True:
            monthDays['Feb'] = 29

        # check month
        if monthValidation(month) == True:
            # check day
            if dayValidation(day) == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# check leap year
def checkLeapYear(year):
    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        return True
    else:
        return False


# final call to check it is valid date or not
if yearValidation(year) == True:
    print(f"{month} {day}, {year} is a valid date.")
else:
    print(f"{month} {day}, {year} isn't a valid date.")

