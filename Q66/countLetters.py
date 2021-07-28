def countLetters(stringWordInput):
    # to count number of letters
    count = 0
    # loop to check each letter
    for i in stringWordInput:
        # ascii value of A-Z and a-z
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            count += 1
    print(f"Number of upper and lower-case letters: {count}")


countLetters("4 + 4 = eight")
