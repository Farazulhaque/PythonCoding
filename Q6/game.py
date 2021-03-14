import random
name = input("What is your name? ")


def rollAgain():
    choice = input("Do you want to roll again? ")
    if choice.lower() == 'yes':
        playerTurn(name)
    elif choice.lower() == 'no':
        print("PlayerTurn returned ", total)
    else:
        print("Whoops!", choice, "isn't a valid hoice. Try again.")
        rollAgain()


def playerTurn(name):
    global total
    roll = random.choice(range(1, 7))
    if roll == 1:
        total = 0
        print(name, "rolled a ", roll)
        print("You pigged out!!")
        print("playerTurn returned 0")
    else:
        total += roll
        print(name, "rolled a ", roll)
        print(name, "earned ", total, "points so far this turn")
        rollAgain()


playerTurn(name)
