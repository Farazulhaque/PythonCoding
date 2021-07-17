# NAME: Pirate Translator
# AUTHOR(s): Mary Marusic
# DATE: month/day/year 07/16/21
# PURPOSE: Translate American English to Pirate language.

# import random module to generate random number
from random import randrange

lineBreak = "#"*60
# printing # for styling
print(lineBreak)

# The holodeck is like virutal reality but you don't need a headset.
print('''\nWelcome to the Star Trek Holodeck! On today's
adventure you will join the crew in sailing the ocean. One
of your stops include Pirate Island and you must use the
translator inlcuded on your tricorder to get around. Enter the
phrase that you would like translated and the translation will
show up on the screen. Enjoy!\n''')

lineBreak = "~"*60
# printing ~ for styling
print(lineBreak)


# main() function
def main():
    '''
    This function controls the entire script......calls on other functions, etc...
    '''
    # print new line
    print()
    # initialise translate variable to 'y' to loop untill translate not equal to 'n'
    translate = 'y'
    while translate != 'n':
        # Execute the try block code and if face any error then execute except block code
        try:
            # get input phrase from user and convert the input to lowercase
            phrase = input('\nEnter your phrase: ').lower()
            # store the value returned by replace(phrase) function into translation variable
            translation = replace(phrase)
            # Printing the returned value or the value stored in translation variable
            print("\nTranslation: ", translation.capitalize())
            # Ask user if want to translate more phrase? and convert to lowercase
            translate = input(
                '\nDo you want to translate more words? Enter [Y/N] ').lower()
            # if user enter something else i.e other than y and n then ask again
            while (translate != 'y') and (translate != 'n'):
                translate = input(('\nEnter y for yes or n for no: ').lower())
        except:
            phrase = input('\nEnter your phrase: ')

    input('\n\nHit Enter to Exit\n')


# replace function to replace the word
def replace(original):
    # replace(oldvalue, newvalue)
    # replace function replaces the old value to new value in the sentence/string
    new = original.replace('hello', 'ahoy')
    new = new.replace(' hi ', 'yo-ho-ho')
    new = new.replace('my', 'me')
    new = new.replace('friend', 'bucko')
    new = new.replace('sir', 'matey')
    new = new.replace('where', 'whar')
    # the space before the letter isolates the word
    new = new.replace(' is', 'be')
    # otherwise output words like 'this' = 'thbe'
    new = new.replace('there', 'thar ')
    new = new.replace('the', "th'")
    new = new.replace('you ', 'ye ')
    new = new.replace('ing', 'in\'')
    new = new.replace('!', '?')

    # generate random number between 0-10
    add = randrange(0, 10)
    # if random number generated is equal to 1
    if add == 1:
        # then add 'Arr' to start of sentence
        new = 'Arr ' + new
    # if random number generated is equal  to 9
    elif add == 9:
        # then add ' arr' to end of sentence
        new = new + ' arr'

    # return the value stored in new variable
    return new


if __name__ == '__main__':
    # calling main()
    main()

# Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))
