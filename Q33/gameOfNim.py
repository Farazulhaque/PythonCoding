import random

stonesLeft = random.randint(15, 30)
stonesToRemove = 0
userTurn = True

print("There are", stonesLeft, "stones")

while stonesLeft > 0:
    while userTurn == True and stonesLeft > 0:

        stonesToRemove = int(input("How many would you like? "))

        if stonesToRemove < 1 or stonesToRemove > 3:
            print("Value must be between 1 and 3.")
        elif stonesLeft - stonesToRemove < 0:
            print("There aren't that many stones left!")  # Give user error!
        else:
            stonesLeft -= stonesToRemove
            print("You takes " + str(stonesToRemove) +
                  " stone(s)! \nThere are " + str(stonesLeft) + " stones.")

            userTurn = False

    while userTurn == False and stonesLeft > 0:

        # Take smaller value between 3 and the stones that are left
        computer = random.randint(1, min(3, stonesLeft))
        stonesLeft -= computer

        print("The computer takes "+str(computer) +
              " stone(s)! \nThere are " + str(stonesLeft) + " stones.")

        userTurn = True

if userTurn == True:
    print("You won the game!")
else:
    print("The computer won the game!")




    
# import random
# stone = random.randint(15, 30)
# while(True):
#     if(stone > 0):
#         user = int(input("There are "+str(stone) +
#                          " stones. How many would you like? "))
#         while(True):
#             if(user < 1 or user > 3):
#                 print("Value must be between 1 and 3")
#                 user = int(input("How many would you like? "))
#             elif (stone < user):
#                 print("Value must be between 1 and "+str(stone))
#                 user = int(input("How many would you like? "))
#         stone = stone-user
#         if(stone > 5):
#             computer = random.randint(1, 3)
#             print("There are "+str(stone) +
#                   " stones. The computer takes "+str(computer)+".")
#             stone = stone-computer
#         elif(stone == 5 or stone == 6):
#             computer = 1
#             print("There are "+str(stone) +
#                   " stones. The computer takes "+str(computer)+".")
#             stone = stone-computer
#         elif(stone == 4):
#             computer = 3
#             print("There are "+str(stone) +
#                   " stones. The computer takes "+str(computer)+".")
#             stone = stone-computer
#         elif(stone == 3):
#             computer = 2
#             print("There are "+str(stone) +
#                   " stones. The computer takes "+str(computer)+".")
#             stone = stone-computer
#         elif(stone == 2):
#             computer = 1
#             print("There are "+str(stone) +
#                   " stones. The computer takes "+str(computer)+".")
#             stone = stone-computer
#         elif(stone == 1):
#             computer = random.randint(1, 1)
#             stone = stone-computer
#             print("You win!")
#             break
#         else:
#             print("The computer wins!")
#             break


