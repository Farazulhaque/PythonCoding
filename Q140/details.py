def main():
    first_name = input("Enter First name: ")
    last_name = input("Enter Last Name: ")
    current_age = input("Enter Current Age: ")
    education_level = input("Enter Education Level: ")
    street_number = input("Enter Street Number: ")
    street_name = input("Enter Street Name: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    zip_Code = input("Enter Zip Code: ")
    phone_number = input("Enter Phone Number: ")
    date_of_birth = input("Enter Date Of Birth: ")
    with open("names.txt", "w") as file:
        file.write("="*250)
        file.write(f"\n%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n" % ("first_name", "last_name",
                   "current_age", "education_level", "street_number", "street_name", "city", "state", "zip_Code", "phone_number", "date_of_birth"))

        file.write("="*250)
        file.write(f"\n%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n" % (first_name, last_name,
                   current_age, education_level, street_number, street_name, city, state, zip_Code, phone_number, date_of_birth))
        file.write("-"*250)
        file.write("\n")


main()
