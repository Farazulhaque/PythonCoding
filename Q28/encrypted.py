inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

infile = open(inputFileName, "r")
outfile = open(outputFileName, "w")

data = infile.readlines()
for code in data:
    plainText = ""
    for ch in code:
        ordValue = ord(ch)
        if (ordValue >= 65 and ordValue <= 122):
            cipherValue = ordValue + distance
            if cipherValue < 0:
                cipherValue = 127 - (distance - (1 - ordValue))
            plainText += chr(cipherValue)
        else:
            plainText += ch
outfile.write(plainText)
outfile.write("\n")

infile.close()
outfile.close()
