def main():
    print("Test.txt file before adding 'hello world' at the end.")
    with open("test.txt", "r") as file:
        for line in file:
            print(line)

    with open("test.txt", "a") as file:
        file.write("hello world")

    print("\nTest.txt file after adding 'hello world' at the end.")
    with open("test.txt", "r") as file:
        for line in file:
            print(line)


main()
