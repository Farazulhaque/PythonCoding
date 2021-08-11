# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words
WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(' ')
    print(" ", len(wordlist), "words loaded.")
    return wordlist

# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = 'claptrap'
letters_guessed = []
space = ""

def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    flag = 0
    for i in letters_guessed:
        if i != secret_word:
            flag = 1
    
    if flag == 0:
        return True
    else:
        return False
    # pass  # This tells your code to skip this function; delete it when you
    # start working on this function


# print_guessed function
def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    global space
    ####### YOUR CODE HERE ######
    empty = "_"
    
    for letter in secret_word:
        space += letter if letter.lower() in letters_guessed else empty
    if space == secret_word:
        print('Congratulations. You guessed the word correctly.')
        exit()
    # pass  # This tells your code to skip this function; delete it when you
    # start working on this function
    print(space)
    # You must config space to None before input again
    space = ''


# play_hangman function
def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to final steps.
    # secret_word = get_word()
    print('Starting game')
    while mistakes_made < MAX_GUESSES:
        guess = input("Guess a character: ")
        if guess in secret_word and guess:
            letters_guessed.append(guess)
            print_guessed()
            if len(space) == len(secret_word):
                if word_guessed():
                    break
        else:
            print("Incorrect guess.")
            mistakes_made += 1
    ####### YOUR CODE HERE ######
    if mistakes_made == MAX_GUESSES:
        print("You didn't guessed the word correctly.")
        print("The secret word is", secret_word)


# Strt the game
play_hangman()