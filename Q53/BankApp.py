def Deposit(amount, bal):
    updated_bal = amount+bal
    return updated_bal


# withdraw function to withdraw amount
def withdraw_bal(amount, bal):
    updated_bal = bal-amount
    return updated_bal


# Show your balance
def show_bal(u_bal, i):
    print("Your balance is: ", u_bal[i])


# change user
def change_user():
    # take usename and password from user
    name = input("Enter Username: ")
    password = input("Enter Password: ")
    return name, password


# open file
namefile = open("UserInformation.txt", "r")
uname = []
u_pass = []
u_bal = []
# read file
for line in namefile:
    global fields
    fields = line.split()
    uname.append(fields[0])
    u_pass.append(fields[1])
    u_bal.append(int(fields[2]))
ip = "D"
name = input("Enter Username: ")
password = input("Enter Password: ")
nameAndPasswordMatched = False
# Loop untill name and password matched
while nameAndPasswordMatched == False:
    for i in range(len(fields)):
        # check name and password is same as the one in file or not
        if(name == uname[i] and password == u_pass[i]):
            # If name and password matched then break the loop by
            # assigning nameAndPasswordMatched = True
            nameAndPasswordMatched = True
            while ip != "E":
                # print menu
                print("\nType D to deposit money")
                print("Type W to withdraw money")
                print("Type B to display Balanace")
                print("Type C to change user,dipslay user name")
                print("Type E to exit")
                # take user choice
                ip = input("\n").upper()

                if(ip == "D"):
                    dep = int(input("Enter amount to deposit: "))
                    # Enter deposit amount again if user enter -ve number
                    while dep < 0:
                        dep = int(input("Enter amount to deposit: "))
                    u_bal[i] = Deposit(dep, u_bal[i])
                    show_bal(u_bal, i)

                elif(ip == "W"):
                    amount = int(input("Enter amount you want to withdraw: "))
                    # Enter withdraw amount again if user enter -ve number
                    while amount < 0:
                        amount = int(
                            input("Enter amount you want to withdraw: "))
                    if(amount < u_bal[i]):
                        show_bal(u_bal, i)
                        u_bal[i] = withdraw_bal(amount, u_bal[i])
                        show_bal(u_bal, i)
                    else:
                        print("Your Withdraw amount is greater than balance: ")

                elif(ip == "B"):
                    show_bal(u_bal, i)

                elif(ip == "C"):
                    name, password = change_user()
                    flag = 0
                    for j in range(len(fields)):
                        if(name == uname[j] and password == u_pass[j]):
                            i = j
                            flag = 1
                    if(flag == 0):
                        print("Invalid username and password")
                        break

                elif(ip == "E"):
                    exit()

                else:
                    print("Invalid")

    # Prompt again if name and password did not matched
    if nameAndPasswordMatched == False:
        print("Please enter correct name and password: ")
        name = input("Enter Username: ")
        password = input("Enter Password: ")

# close file
namefile.close()
