def convertTemp(fahrenheit):
    try:
        celsius = (fahrenheit - 32) / 1.8
        return celsius
    except:
        print("ERROR: Input value is not supported")


def main():
    try:
        infile = open("tempdata.txt", "r")
        for line in infile:
            line = line.strip()
            celsius = convertTemp(float(line))
            print("{:.2f}".format(celsius))
    except:
        print("ERROR: File can't open")


main()
