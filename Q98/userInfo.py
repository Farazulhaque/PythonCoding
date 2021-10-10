def getUserInfo():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    email = input("What is your email address? ")

    with open("userInfo.txt", 'a') as file:
        file.write(f"%-10s {name}" % "Name:")
        file.write("\n")
        file.write(f"%-10s {age}" % "Age:")
        file.write("\n")
        file.write(f"%-10s {email}" % "Email:")
        file.write("\n")


getUserInfo()
