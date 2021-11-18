import pyperclip


def encrypt(message, key):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    global translated
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
        if translatedIndex <= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        elif translatedIndex < 0:
            translated = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    # guv6 v6 z! 6rp5r7 zr66ntr.
    print(translated)
    pyperclip.copy(translated)


def decrypt(message, key):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    global translated
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
        if translatedIndex < len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        elif translatedIndex < 0:
            translated = translatedIndex - len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    # guv6 v6 z! 6rp5r7 zr66ntr.
    print(translated)
    pyperclip.copy(translated)


def main():
    # message = 'This is my secret message.'
    # key = 13
    # mode = 'decrypt'
    message = ""

    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        # loop in each line
        for line in file:
            message += line
    mode = input("Enter encrypt or decrypt: ")
    key = int(input("Enter key: "))

    if mode == 'encrypt':
        encrypt(message, key)
    elif mode == 'decrypt':
        decrypt(message, key)

    outFile = input("Enter output filename: ")
    with open(outFile, "w") as file:
        file.write(translated)


main()
