def print_menu():
    print("\tMenu")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q – Quit")


def execute_menu(choice, string):
    if choice == "c":
        print(
            f"Number of non-whitespace characters are {get_num_of_non_WS_characters(string)}")
    elif choice == "w":
        print(f"Number of words are {get_num_of_words(string)}")
    elif choice == "f":
        print(
            f"String after fixing capitalization are {fix_capitalization(string)}")
    elif choice == "r":
        print(
            f"String after replacing punctuations are {replace_punctuation(string, exclamation_count=0, semicolon_count=0)}")
    elif choice == "s":
        print(f"String after fixing spaces are {shorten_space(string)}")
    else:
        exit(0)


def get_num_of_non_WS_characters(string):
    chars = 0
    for i in string:
        if i != " ":
            chars += 1
    return chars


def get_num_of_words(string):
    wordlist = string.split()
    num_of_words = len(wordlist)
    return num_of_words


def fix_capitalization(string):
    return string.capitalize()


def replace_punctuation(string, exclamation_count, semicolon_count):
    newString = ""
    for char in string:
        if char == "!":
            newString += "."
            exclamation_count += 1
        elif char == ";":
            newString += ","
            semicolon_count += 1
        else:
            newString += char

    print(
        f"Number of times Exclamation(!) is replaced are {exclamation_count}")
    print(f"Number of times Semicolon(;) is replaced are {semicolon_count}")

    return newString


def shorten_space(string):
    newString = " ".join(string.split())

    return newString


def main():
    string = input("Enter text: ")
    print_menu()
    choice = input("Enter your choice: ").lower()
    loop = True
    while loop == True:
        while choice not in ["c", "w", "f", "r", "s", "q"]:
            choice = input("Enter your choice: ").lower()
        execute_menu(choice, string)
        choice = input("Enter your choice: ").lower()


main()
