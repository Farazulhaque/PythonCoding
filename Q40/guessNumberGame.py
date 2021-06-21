# import only system from os
from os import system

import random


def main():
    # For clearing the screen
    system('cls')
    # For adding blank line
    blank_line = '\n'*1

    print('Welcome to the Guess number game!')
    print(blank_line)
    player_name = input("What is your name? ")
    print(blank_line)

    # to start the loop initially try_again = 'y'
    try_again = 'y'
    # Count number of guesses by player
    number_of_guesses = 0

    while (try_again.lower() == 'y'):
        # Get number of times player want to guess
        guess_limit = input("How many times would you like to play? ")
        # If player enter nothing and hit enter
        # then default value of guess_limit is 15
        if guess_limit == "":
            guess_limit = 15
        # Convert the guess_limit to int data type
        guess_limit = int(guess_limit)
        # If user inputted number then go inside this try block
        # else go inside except block
        try:
            # Generate random number in betwee 1-99 to be guess by the player
            number = random.randint(1, 99)
            # Loop untill there is no guesses left
            while (guess_limit != 0):
                # Player guess
                guess = int(input("Enter an integer from 1 to 99: "))
                # Check for valid number i.e number should be betwee 1 - 99
                while ((guess < 1) or (guess > 99)):
                    guess = int(
                        input("ERROR! Please enter an integer in the range from 1 to 99: "))

                # Check for High and low guess
                if guess < number:
                    print("Guess is low")
                elif guess > number:
                    print("Guess is high")
                # If it is neither high nor low
                else:
                    print(blank_line)
                    print("YOU WIN! You made " +
                          str(number_of_guesses) + " guesses.")
                    # To get out of the loop
                    break
                # decrement the guess_limit by 1 on every iteration
                guess_limit -= 1
                print(guess_limit, 'guesses left')
                # Increment number of guesses by the player
                number_of_guesses += 1
                print()
                # If guess_limit is equal to 0, it means player have not guessed the number
                # And player lose
                if guess_limit == 0:
                    print("YOU LOSE! You made " +
                          str(number_of_guesses) + " guesses.")
        except ValueError:
            print('ERROR: Non-numeric data. Please enter valid number!')
            print(blank_line)
        # Ask again to play again
        # If player enter anything other than 'Y' or 'y' then exit the game
        try_again = input("Play again? Enter 'Y' or 'y' for yes: ")
        print(blank_line)


main()
