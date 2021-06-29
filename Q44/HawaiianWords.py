# Set the values that are checked for the while looping
continuePronouncingWords = True
incorrectWord = True
twoLetterDictionary = {'ai': 'eye-', 'ae': 'eye-', 'au': 'ow-', 'aw': 'ah-w', 'ei': 'ay-', 'eu': 'eh-oo-',
                       'ew': 'eh-v', 'iu': 'ew-', 'iw': 'ee-v', 'oi': 'oy-', 'ou': 'ow-', 'ow': 'oh-w', 'ui': 'ooey-', 'uw': 'oo-w'}
singleLetterDictionary = {'a': 'ah-', 'e': 'eh-',
                          'i': 'ee-', 'o': 'oh-', 'u': 'oo-'}

# Start the while loop for pronouncing words
while continuePronouncingWords:
    # Set base variables for each time looping
    pronunciationOfHawaiianWord = ''
    hawaiianWordToPronounce = ''
    loopCountForWord = 0
    skipLetter = False
    incorrectWord = True
    # Start the while loop for entering a invalid Hawaiian word
    while incorrectWord:
        # Get word to pronounce
        hawaiianWordToPronounce = input(
            "Enter a Hawaiian word to pronouce ==> ").lower()
        # Loop through word for incorrect lettering
        for letterInHawaiianWord in hawaiianWordToPronounce:
            # Check for non Hawaiian letters
            if not letterInHawaiianWord == 'p' and not letterInHawaiianWord == 'k' and not letterInHawaiianWord == 'h' and not letterInHawaiianWord == 'l' and not letterInHawaiianWord == 'm' and not letterInHawaiianWord == 'n' and not letterInHawaiianWord == 'w' and not letterInHawaiianWord == 'a' and not letterInHawaiianWord == 'e' and not letterInHawaiianWord == 'i' and not letterInHawaiianWord == 'o' and not letterInHawaiianWord == 'u' and not letterInHawaiianWord == ' ' and not letterInHawaiianWord == "'":
                # Print incorrect letter and break loop, color for better readability
                print(letterInHawaiianWord, 'is not a valid Hawaiian character.')
                incorrectWord = True
                break
            # Break while loop for inputting Hawaiian word
            incorrectWord = False

    # Loop through word to pronounce and set pronounced word
    for letterInHawaiianWord in hawaiianWordToPronounce:
        # Checking for a letter skip
        if not skipLetter:
            # If a letter without special sounding, then add it
            if letterInHawaiianWord == 'p' or letterInHawaiianWord == 'k' or letterInHawaiianWord == 'h' or letterInHawaiianWord == 'l' or letterInHawaiianWord == 'm' or letterInHawaiianWord == 'n' or letterInHawaiianWord == 'w':
                pronunciationOfHawaiianWord += letterInHawaiianWord
            # If the letter is ', then remove the previous - and add the quote
            elif letterInHawaiianWord == "'":
                if pronunciationOfHawaiianWord[len(pronunciationOfHawaiianWord)-1] == '-':
                    pronunciationOfHawaiianWord = pronunciationOfHawaiianWord[:-1].capitalize(
                    )
                pronunciationOfHawaiianWord += "'"
            # If the letter is a space, then remove the previous - and add the space
            elif letterInHawaiianWord == ' ':
                if pronunciationOfHawaiianWord[len(pronunciationOfHawaiianWord)-1] == '-':
                    pronunciationOfHawaiianWord = pronunciationOfHawaiianWord[:-1].capitalize(
                    )
                pronunciationOfHawaiianWord += ' '
            else:
                # Loop through the special double sounding letters and add to the result.
                for setDiction in twoLetterDictionary:
                    if hawaiianWordToPronounce[loopCountForWord:loopCountForWord+2] == setDiction:
                        pronunciationOfHawaiianWord += twoLetterDictionary[setDiction]
                        skipLetter = True
                        break
                # Loop through the special single sounding letters and add to the result.
                if not skipLetter:
                    for setDiction in singleLetterDictionary:
                        if letterInHawaiianWord == setDiction:
                            pronunciationOfHawaiianWord += singleLetterDictionary[setDiction]
                            break
        elif skipLetter:
            skipLetter = False

        loopCountForWord += 1
    # Remove the extra - at the end of the pronounced word
    if pronunciationOfHawaiianWord[len(pronunciationOfHawaiianWord)-1] == '-':
        pronunciationOfHawaiianWord = pronunciationOfHawaiianWord[:-1].capitalize(
        )
    # Print out the pronunciation of the Hawaiian word
    print(hawaiianWordToPronounce.upper(),
          'is pronouced', pronunciationOfHawaiianWord)
    # Ask if they want to get another pronunciation of a Hawaiian word

    innerloop = True
    while innerloop:
        pronounceAnotherWord = input(
            'Do you want to input another word? Y/N/YES/NO ==> ')
        if (pronounceAnotherWord.upper() in ["Y", "YES", "N", "NO"]):
            innerloop = False
        else:
            print("Enter Y, YES, N or NO")
    if (pronounceAnotherWord.upper() in ["N", "NO"]):
        break
