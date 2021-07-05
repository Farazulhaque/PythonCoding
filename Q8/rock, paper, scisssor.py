from random import randint

# assign a random play to the computer
computer = randint(0, 2)

# set player to False
player = False
comp = 0
you = 0
tie = 0
while player == False:

    print("Let's play Rock, Paper, Scissor! \nMake your selection: \n(1 for Rock, 2 for Paper, 3 for Scissors, 0 to end)")
    player = int(input(">>> "))

    if player == 1:
        print("You chose rock.", end=" ")
        if computer == 1:
            print("The computer chose rock. It's a tie!")
            tie += 1
        elif computer == 2:
            print("The computer chose paper. You lose!")
            comp += 1
        else:
            print("The computer choses scissors. You win!")
            you += 1
        player = False
    elif player == 2:
        print("You chose paper.", end=" ")
        if computer == 1:
            print("The computer chose rock. You win!")
            you += 1
        elif computer == 2:
            print("The computer chose paper. It's a tie!")
            tie += 1
        else:
            print("The computer choses scissors. You lose!")
            comp += 1
        player = False
    elif player == 3:
        print("You chose scissor.", end=" ")
        if computer == 1:
            print("The computer chose rock. You lose!")
            comp += 1
        elif computer == 2:
            print("The computer chose paper. You win!")
            you += 1
        else:
            print("The computer choses scissors. It's a tie!")
            tie += 1
        player = False
    elif player == 0:
        print("You won " + str(you) + " time")
        print("The computer won " + str(comp) + " time")
        print("You tied with the computer " + str(tie) + " time")
        print("Thanks for playing! Goodbye")
        player = True
    else:
        print("Invalid selection. ")
        player = False

    computer = randint(0, 2)
