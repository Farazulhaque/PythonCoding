def main():  # 6 used main function
    filename = "ENEL2CMInfo"
    listlines = []
    print()
    try:                                        # Used try except block to except any error
        num_lines = 1
        with open(filename, 'r') as f:  # 4 Reopen the file
            for line in f:  # 5 Using a loop, count and print the contents of the file
                # Used rstrip to strips a character from end of the string
                line = line.rstrip('\n')
                listlines.append(line)
                num_lines += 1
        num_lines -= 1
        x = input("Enter number of lines you want to print: ")
        x = int(x)
        if x <= num_lines:
            for i in range(x):
                print(listlines[i])
        else:
            print("Invalid number of lines")

    except FileNotFoundError:
        print("The filename you typed is not available")


if __name__ == "__main__":
    main()
