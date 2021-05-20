player1 = input("Player1: ")

# Initializing the number of guesses.
count = 1
def main(count = 1):
    # player 2 guess
    player2 = input("player2: Take a guess: ")

    def rand_call(player2,count):
        # Comparing the guessed color with the player1 color
        if player1 == player2:
            print("Congratulations you guessed the color correctly.")
            print("Total number of guesses: ", count)
            loop = False
        else:
          count += 1
          main(count)

    rand_call(player2,count)  # calling the function rand_call with argument player2
main()