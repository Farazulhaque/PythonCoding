def main():                                     #6 used main function
    filename = input("Enter the name of the file to open for read: ")
    print()
    try:                                        # Used try except block to except any error
        file = open(filename, "r")              #1 Read a filename
        print("The contents of the data file " +
              filename + " are listed below ", end='\n\n')
        print(file.read(), end='\n\n')          #2 Read the contents of the file using read function
        file.close()                            #3 Close the file
        print("closing ", filename)
        print()
        print("==============================")
        print("Reopening ", filename, end='\n\n')
        num_lines = 1
        with open(filename, 'r') as f:          #4 Reopen the file
            for line in f:                      #5 Using a loop, count and print the contents of the file
                line = line.rstrip('\n')        # Used rstrip to strips a character from end of the string
                print("Lines ", str(num_lines), line)
                num_lines += 1
        num_lines -= 1
        print()
        print("There are ", str(num_lines),
              " lines in file ", filename, end='\n')
    except FileNotFoundError:
        print("The filename you typed is not available")


if __name__ == "__main__":
    main()
