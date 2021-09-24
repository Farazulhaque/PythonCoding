import random

# store fruits in list
fruits = ["apple", "grape", "guava", "lemon",
          "nance", "peach", "prune", "salak"]

# get random fruit
word = random.choice(fruits)
# print(word)
print("Guess This Five-Letter Fruit!")

# max attempt is 5
turns = 5
# to store guesses
guesses = ''

# loop until turns is greater than 0
while turns > 0:
    # get user input
    print()
    guess = input("Guess a Character: ")
    # add to guesses string
    guesses += guess
    # check if guessed character is in word or not
    if guess not in word:
        print(f"Wrong! {turns-1} guess(es) left.")

    # check if all characters are guessed
    new = ""
    for char in word:  # This will enter letter in word
        if char in guesses:
            print(char, " ", end="")
            new += char
        else:
            print("_ ", end="")
    print()
    # compare both new and random fruit
    if new == word:
        print("\nYou Won!")
        print(f"The word is {word}")
        break

    turns -= 1

# if no turns left
if turns == 0:
    print("\nYou Lose!")
    print(f"The word is {word}")
