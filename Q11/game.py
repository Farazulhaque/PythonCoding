import random

# Category types
categories = {1: "Fruits", 2: "Colors"}

# Words in each categoy
words_inCat = {"Fruits": ["Apple", "Banana", "Watermelon", "Pineapple", "Orange", "Tomato", "Grapefruit", "Dragonfruit"], "Colors": [
    "Green", "Blue", "Yellow", "Orange", "Turquoise", "Lavender", "Magenta", "Chartreuse"]}

# Hangman Display Function


def hangman(mistake):
    print("|____\n" +
          "| |\n" +
          "|\n" +
          "|\n" +
          "|\n")
    if(mistake == 1):
        print("|____\n" +
              "| |\n" +
              "| O\n" +
              "|\n" +
              "|\n" +
              "|\n")
    if(mistake == 2):
        print("|____\n" +
              "| |\n" +
              "| O\n" +
              "| |\n" +
              "|\n" +
              "|\n")
    if(mistake == 3):
        print("|____\n" +
              "| |\n" +
              "| O\n" +
              "| \|\n" +
              "|\n" +
              "|\n")
    if(mistake == 4):
        print("|____\n" +
              "| |\n" +
              "| O\n" +
              "| \|/\n" +
              "|\n" +
              "|\n")
    if(mistake == 5):
        print("|____\n" +
              "| |\n" +
              "| O\n" +
              "| \|/\n" +
              "| /\n" +
              "|\n")
    if(mistake == 6):
        print("|____\n" +
              "| |\n" +
              "| O\n" +
              "| \|/\n" +
              "| / \ \n" +
              "|\n")


# Intro
userName = input("Please enter your name: ")
print("Hello", userName, "lets play a game of Hangman!\n")


# Loop until get valid category
while True:
    try:
        for key, value in categories.items():
            print("Enter " + str(key) + " for " + str(value))
        choice = int(input("Enter your choice = ").strip())
        if choice not in categories.keys():
            raise ValueError
        break
    except ValueError:
        print("\nInvalid Selection")


# main function of the game
def main(choice, categories):
    # Word and difficulty selection
    word = random.choice(words_inCat[categories[choice]])

    def check_difficult():
        difficulty = input(
            "\nEnter which difficulty you want: NORMAL, HARD: ").strip().upper()
        word = ""
        while True:
            word = random.choice(words_inCat[categories[choice]])
            if (difficulty == "HARD" and len(word) > 6) or (difficulty != 'HARD' and len(word) <= 6):
                break
        return difficulty

    # Difficulty Selection Criteria
    diff = check_difficult()
    if diff == "HARD" or diff == "NORMAL":
        pass
    else:
        print("Invalid Selection\n")
        check_difficult()

    # Gameplay
    empty = "_"
    space = empty*len(word)
    found = ""
    mistakes = 0
    while empty in space and mistakes < 6:
        print("You have", 6 - mistakes, "guesses left")
        guess = input("(Guess) Enter a letter in word " +
                      space + '>').strip().lower()
        if guess not in word.lower():
            print("\t", guess, "is not in the word")
            mistakes += 1
            hangman(mistakes)
        elif guess in space:
            print("\t", guess, "is already in the word")
        else:
            found += guess
            space = ""
            for letter in word:
                space += letter if letter.lower() in found else empty

    # Win or lose screen
    while True:
        if mistakes < 6:
            print("\nThe word is", word, " Congratulations, you win!")
            break
        else:
            print("\nThe word is", word, " Sorry, you lose")
            break

    # Continue Game?
    continueGame = input(
        "\nWould you like to play again? Type Y for yes, Any other key to quit\n")
    if continueGame.upper() == "Y":
        # User Category Selection/Continue Game Loop
        while True:
            try:
                # Category types
                categories = {1: "Fruits", 2: "Colors"}
                for key, value in categories.items():
                    print("Enter " + str(key) + " for " + str(value))
                choice = int(input("Enter your choice = ").strip())
                if choice not in categories.keys():
                    raise ValueError
                main(choice, categories)
                break
            except ValueError:
                print("\nInvalid Selection")
    else:
        print("Thanks for playing")


# function call for only first time
main(choice, categories)
