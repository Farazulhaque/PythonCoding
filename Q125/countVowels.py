def count(word):
    # all upper case and lower case vowels and consonants
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel = 0
    consonant = 0
    letters = 0

    for letter in word:
        # check each letter in vowels string
        # if in vowels then add to vowel count
        if letter in vowels:
            vowel += 1
        # if in consonants then add to consonant count
        elif letter in consonants:
            consonant += 1
        # increment letter on each iteration
        letters += 1

    print(f"Word: {word}")
    print(f"Number number of Vowels: {vowel}")
    print(f"Number number of Consonants: {consonant}")
    print(f"Total number of Letters: {letters}")


def main():
    word = input("Enter a word: ")
    if word != "":
        count(word)
    else:
        import random
        words = ["stay", "spade", "sleepy", "plucky", "steer",
                 "coil", "purring", "airplane", "resolute", "cent"]
        word = words[random.randint(0, len(words))]
        count(word)


main()
