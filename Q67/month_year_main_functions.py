def main():
    name = input("Enter your name: ")
    month = get_month()
    year = get_year()
    season = find_season(month)
    leap_year = is_leap_year(year)

    print(
        f"Hello, {name}! You were born in the {season} and {year} {leap_year}")

    cents = int(input("How many pennies are in your penny jar? "))
    denominations = penny_jar(cents)


def get_month():
    while True:
        month = int(
            input("Enter the month number in which you were born 1 - 12: "))
        if (month < 1 or month > 12):
            print("Invalid Month! Enter again.")
        else:
            return month


def get_year():
    while True:
        year = int(input("Enter the year in which you were born: "))
        if year < 0:
            print("Invalid Year! Enter again.")
        else:
            return year


def find_season(month):
    if (month == 1 or month == 2 or month == 12):
        return "winter"
    elif (month == 3 or month == 4 or month == 5):
        return "spring"
    elif (month == 6 or month == 7 or month == 8):
        return "summer"
    else:
        return "fall"


def is_leap_year(year):
    if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        return "was a leap year."
    else:
        return "was not a leap year."


def penny_jar(cents):
    dollars = int(cents/100)
    cents = cents - (dollars*100)
    quarters = int(cents/25)
    cents = cents - (quarters*25)
    dimes = int(cents/10)
    cents = cents - (dimes*10)
    nickels = int(cents/5)
    cents = cents - (nickels*5)
    pennies = cents
    print(f"You will get: \n{dollars} Dollars \n{quarters} Quarters \n{dimes} Dimes \n{nickels} Nickels \n{pennies} Pennies")


main()
