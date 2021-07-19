def main():
    full_name = get_full_name()
    password = get_password()
    email = get_email()
    phone = get_phone_number()
    first_name = get_first_name(full_name)
    print()
    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"We'll text your confirmation code to this number: {phone}")


def get_full_name():
    while True:
        name = input("Enter full name: ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password: ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(
                "Password must be 8 characters or more \nwith at least one digit and one uppercase letter.")
        else:
            return password


def get_email():
    while True:
        email = input("Enter email address: ")
        attherate_found = False
        for char in email:
            if char == "@":
                attherate_found = True
        if attherate_found == True and email[-4:] == ".com":
            return email
        else:
            print("Please enter a valid email address")


def get_phone_number():
    while True:
        phone = input("Enter phone number: ")
        pnum = ""
        containAlpha = False
        for i in range(len(phone)):
            if phone[i].isnumeric() == True:
                pnum += phone[i]
            elif phone[i].isalpha() == True:
                containAlpha = True
        if len(pnum) == 10 and containAlpha == False:
            return phone
        else:
            print("Please enter a 10 digit phone number")


if __name__ == "__main__":
    main()
