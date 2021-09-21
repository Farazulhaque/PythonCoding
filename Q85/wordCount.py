def openFile():
    done = False
    while not done:
        try:
            fileName = input("Please enter the file name: ")
            data = readFile(fileName)
            return data
        except IOError:
            print("Error: file not found.")
        except ValueError:
            print("Error: file contents invalid.")
        except RuntimeError as error:
            print("Error:", str(error))


def readFile(fileName):
    fileOpen = open(fileName, "r")
    try:
        return modFile(fileOpen)
    finally:
        fileOpen.close()


def modFile(fileOpen):
    wordList = []
    for line in fileOpen:
        line = line.strip("\n")
        line = line.lower()
        wordList.sort()
        wordList.append(line)
    outFile = open("words.count", "a")
    unique = set(wordList)
    for word in unique:
        wordList.count(word)
        outFile.write(str(wordList) + ":" + str(wordList.count(word)))
    outFile.close()


def main():
    openFile()
    print("File Reading, Sorting, and Counting Completed")


main()
