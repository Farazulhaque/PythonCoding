def main():
    # get user input username and password to check in accounts.txt
    uname = input("Username: ")
    paswd = input("Password: ")

    # initialise boolean variable to false
    exists = False
    # open file to read
    with open("accounts.txt") as file:
        # read line by line
        for eachLine in file:
            # split by ':' and store in cred list
            cred = eachLine.split(":")
            # check condition
            # rstrip to remove \n from each line
            if (uname == cred[0] and paswd == cred[1].rstrip()):
                print("Welcome")
                # and assign true to boolean variable
                exists = True
                exit()

    # if boolean variable is still false then it means that
    # the condition above in for loop is not becomes true
    if exists == False:
        # so print login failed and
        print("Login Failed")
        # call main() to get user input again
        main()


main()
