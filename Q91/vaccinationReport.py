txt = "Welcome to Vaccination Center"
x = txt.center(50)
print(x)

fname = input("Enter First name: ")
lname = input("Enter Last Name: ")

day = int(input("Enter Day of Birth: "))
while day > 31 or day < 1:
    day = int(input("Enter Day of Birth: "))

month = int(input("Enter Month of Birth: "))
while month > 12 or month < 1:
    month = int(input("Enter Month of Birth: "))

year = int(input("Enter Year of Birth: "))
while year > 2006 or year < 1920:
    year = int(input("Enter Year of Birth: "))


vday = int(input("Enter Day of Vaccination: "))
while vday > 31 or vday < 1:
    vday = int(input("Enter Day of Vaccination: "))

vmonth = int(input("Enter Month of Vaccination: "))
while vmonth > 12 or vmonth < 1:
    vmonth = int(input("Enter Month of Vaccination: "))

vyear = int(input("Enter Year of Vaccination: "))
while vyear > 2021 or vyear < 2020:
    vyear = int(input("Enter Year of Vaccination: "))

vname = input("Enter name of Vaccination: ")
centerOfVaccination = input("Enter center of the Vaccination: ").capitalize()
lotOfVaccination = input("Enter lot of Vaccination: ")


# ----------------------------------------------------------------------------
# Generating Report
print()
print(f"%-30s: {fname} {lname}" % ("Name"))
print(f"%-30s: {day}/{month}/{year}" % ("Date Of Birth"))
print(f"%-30s: {vday}/{vmonth}/{vyear}" % ("Date Of Vaccination"))
print(f"%-30s: {vname}" % ("Name Of Vaccination"))
print(f"%-30s: {centerOfVaccination}" % ("Center Of Vaccination"))
print(f"%-30s: {lotOfVaccination}" % ("Lot Of Vaccination"))
print("-----------------------------------------------")
print("\nThank you for choosing our services.")
print("Report generated successfully.")
