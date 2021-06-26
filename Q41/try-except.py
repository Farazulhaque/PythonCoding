menu = ['Category', 'Item', 'Serving Size',
        'Calorie', 'Calories from Fat', 'Quit']

def printMenu():
    for i in range(len(menu)):
        print(i+1, menu[i])

    choice = int(input("Enter your choice: "))
    while (choice < 1 or choice > 6):
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("ERROR: you did not enter a number")
            choice = int(input("Enter your choice: "))
    return choice

def main():
    user = printMenu()
    print("The user entered:", user)

main()

