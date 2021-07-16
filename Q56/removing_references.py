def main():                                     # main function
    file1 = input("Enter the name of the file to open for read: ")
    # file1 = "python_history.txt"
    file2 = input("Enter name of the file to write formatted content: ")
    remove_ref(file1, file2)


def remove_ref(file1, file2):
    try:                                        # Used try except block to except any error
        count = 0                               # To count number of references
        with open(file1, 'r') as f1:            # open the file to read
            with open(file2, "a") as f2:
                for line in f1:
                    line = line.rstrip('\n')    # Used rstrip to strips a character from end of the string
                    flag = 0
                    for i in range(len(line)):
                        if line[i] == "[":
                            flag = 1
                        elif flag == 1:
                            if line[i] == "]":
                                flag = 0
                                count += 1
                        else:
                            f2.write(line[i])
                            flag = 0

        print(f"Formatting {file1}")
        print(f"No of references: {count}")
        print()
        print()
        file = open(file2, "r")
        print(file.read(), end="\n\n")
        file.close()
    except FileNotFoundError:
        print("The file1 you typed is not available")


if __name__ == "__main__":
    main()
