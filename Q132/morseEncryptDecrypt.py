letters = []
morsecode = []


def readFile():
    with open("Q113\morsetext.txt", "r") as file:
        for line in file:
            lst = line.split(" : ")
            letters.append(lst[0])
            morsecode.append(lst[1].replace("\n", ""))
            # print(lst)


def textToMorse():
    print("Please enter a text to translate: ")
    text = input().upper()
    # text = "To be or not to be".upper()
    for char in text:
        if char == " ":
            print("  ", end="")
        else:
            i = letters.index(char)
            morse = morsecode[i]
            print(morse, end=" ")
    print("\n\n")


def morseToText():
    print("Please enter morse to translate: ")
    morse = input()
    # morse = "- ---   -... .   --- .-.   -. --- -   - ---   -... ."
    words = morse.split("   ")
    for i in range(len(words)):
        code = words[i].split(" ")
        for j in code:
            letter = morsecode.index(j)
            print(letters[letter], end="")
        print("", end=" ")
    print("\n\n")


def main():

    readFile()
    while True:
        print("Hello, this program allows you to translate text to morse code or translate morse code to text.\n")
        print("Please, select one of the below options: \n")
        print("*** Enter 't' for encoding text")
        print("*** Enter 'm' for decoding morse code")
        print("*** Enter 'e' to exit program.\n")

        inp = input("My input is: ")
        while inp not in ['t', 'm', 'e']:
            print("***invalid option***")
            inp = input("Please enter a valid option: ")

        if inp == 't':
            textToMorse()
        elif inp == 'm':
            morseToText()
        else:
            exit(0)


main()
