letters = []
morsecode = []

with open("Q113\morsetext.txt", "r") as file:
    for line in file:
        lst = line.split(" : ")
        letters.append(lst[0])
        morsecode.append(lst[1].replace("\n", ""))
        print(lst)


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
    print("Please enter a text to translate: ")
    text = input().upper()
    for char in text:
        if char == " ":
            print("  ", end="")
        else:
            i = letters.index(char)
            morse = morsecode[i]
            print(morse, end=" ")
            
if inp == 'm':
    print("Please enter morse to translate: ")
    morse = input()
    for i in range(len(morse)):
        if i < (len(morse) -3):
            if morse[i] == " " and morse[i+1] == " " and morse[i+1] == " ":
                print(" ", end="")
                i += 2
        if morse[i] == " ":
            print("", end = "")
        else:
            j = morse.index(morse[i])
            letter = letters[j]
            print(letter, end=" ")
