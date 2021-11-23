FILENAME = input("Enter file name: ")
OUTPUTFILENAME = "cs521_3_4_output.txt"
WORDSALLOWED = 20
WORDSPERLINE = 5

try:
    with open(FILENAME, "r") as infile:
        # loop in each line
        wordscount = 0
        words = []
        for line in infile:
            wordscount += len(line.split())
            words += line.split()
        # print(wordscount)
        # print(words)
        if wordscount != WORDSALLOWED:
            print("ERROR: file has a different number of words")
        else:
            with open(OUTPUTFILENAME, 'w') as outfile:
                wordCount = 0
                for i in range(len(words)):
                    outfile.write(words[i] + " ")
                    wordCount += 1
                    if wordCount % 5 == 0:
                        outfile.write("\n")
                print(f"Success! Output written to: {OUTPUTFILENAME}")


except FileNotFoundError:
    print(f"Unexpected error opening {FILENAME}")

