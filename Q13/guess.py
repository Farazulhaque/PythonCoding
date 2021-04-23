import random

# Taking range
lower = 1
upper = 100

# generating random number between the lower and upper limit
x = random.randint(lower, upper)
print("MAIN MENU")
print("----------------\n")
print("\t 1) Play Game")
print("\t 2) Exit\n")


loop = True
while loop == True:
    # taking guessing number as input
    guess = int(input("Enter a number between 1 and 100"))

    def rand_call(guess):
        # Comparing the guessed number with the random number generated b/w 1-100
        if x == guess:
            print("Congratulations!!!")
        elif x > guess:
            print("Too low, try again")
        elif x < guess:
            print("Too high, try again")

    rand_call(guess)

    if x == guess:
        play_again = int(input("Would you like to play again? (1 - yes, 2 - no) "))
        # generate random number again
        x = random.randint(lower, upper)
        if play_again == 2:
            loop = False
        else:
            loop = True
