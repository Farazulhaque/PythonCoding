def pd_get_num_of_non_WS_characters(usrStr):
    return len(usrStr.replace(' ', ''))


def pd_get_num_of_words(usrStr):
    return len(usrStr.split())


def pd_fix_capitalization(usrStr):
    result = ''
    count = 0
    newSentence = True
    for c in usrStr:
        if newSentence:
            if c.islower():
                c = c.upper()
                newSentence = False
                count += 1
            elif c.isupper():
                newSentence = False
            result = result + c
            if c in '.!?':
                newSentence = True
            return result, count


def pd_shorten_space(usrStr):
    result = ' '.join(usrStr.split())
    return result


def pd_replace_punctuation(usrStr, ** kwargs):
    result = ''
    for c in usrStr:
        if c == '!':
            kwargs['exclamation_count'] += 1
            c = '.'
        elif c == ';':
            kwargs['semicolon_count'] += 1
            c = ','
        result += c
        print('Punctuation replaced')
        print('exclamation_count:', kwargs['exclamation_count'])
        print('semicolon_count:', kwargs['semicolon_count'])
        return result


def readFromFile(file_name):
    try:
        r = open(file_name, "r")
        usrStr = ''
        for x in r:
            usrStr = usrStr+x
        return usrStr
    except:
        print('Error reading file\n')


def writeToFile(file_name, usrStr):
    try:
        f = open(file_name, "w")
        f.write(usrStr)
        print('Wrote to file')
        f.close()
    except:
        print('Error writing file\n')


def print_menu(usrStr):
    menu = '''MENU
    c - Number of non-whitespace characters
    w - Number of words
    f - Fix capitalization
    r - Replace punctuation
    s - Shorten spaces
    q - Quit
    o - Open file and read input
    S - Save text

    Choose an option:'''

    print(menu)
    menuOp = input()

    if menuOp == 'c':
        n = pd_get_num_of_non_WS_characters(usrStr)
        print('Number of non-whitespace characters:', n)
        print()

    elif menuOp == 'w':
        m = pd_get_num_of_words(usrStr)
        print('Number of words:', m)
        print()

    elif menuOp == 'f':
        usrStr, count = pd_fix_capitalization(usrStr)
        print('Number of letters capitalized:', count)
        print('Edited text:', usrStr)
        print()

    elif menuOp == 's':
        usrStr = pd_shorten_space(usrStr)
        print('Edited text:', usrStr)
        print()

    elif menuOp == 'r':
        usrStr = pd_replace_punctuation(
            usrStr, exclamation_count=0, semicolon_count=0)
        print('Edited text:', usrStr)
        print()

    elif menuOp == 'o':
        file_name = input('Enter file name: ')
        usrStr = readFromFile(file_name)
        print('Text from file:', usrStr)
        print('')

    elif menuOp == 'S':
        file_name = usrStr.split(".")[0]+"-new.txt"
        writeToFile(file_name, usrStr)

    elif menuOp == 'q':
        return menuOp, usrStr

    else:
        print_menu(usrStr)

    return menuOp, usrStr


if __name__ == '__main__':

    usrStr = input('Enter a sample text:')
    print()
    print()
    print('You entered:', usrStr)
    print()
    m = ''
    while m.lower() != 'q':
        m, usrStr = print_menu(usrStr)
