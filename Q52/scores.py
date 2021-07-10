def getChoice():
    while True:
        print("1. Read scores")
        print("2. Convert scores to a letter grade and display it")
        print("3. Show statistics (minimum, maximum, statistics)")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            readScores()
        elif choice == 2:
            showLetterGrade()
        elif choice == 3:
            showStatistics()
        elif choice == 4:
            exit = input("Are you sure?(y/n) ")
            if exit.lower() == "y":
                break
            else:
                getChoice()


def readScores():
    global scores
    global minimum
    global maximum
    global total
    global average
    scores = []
    n = int(input("Enter number of scores: "))
    for i in range(n):
        x = int(input("Enter score: "))
        scores.append(x)
    minimum = min(scores)
    maximum = max(scores)
    total = sum(scores)
    average = total / len(scores)


def showLetterGrade():
    print("Percentage\tLetter grade")
    for i in range(len(scores)):
        if scores[i] < 60:
            print(f"   {scores[i]}   \t\tF")
        elif scores[i] < 69:
            print(f"   {scores[i]}   \t\tD")
        elif scores[i] < 79:
            print(f"   {scores[i]}   \t\tC")
        elif scores[i] < 89:
            print(f"   {scores[i]}   \t\tB")
        elif scores[i] <= 100:
            print(f"   {scores[i]}   \t\tA")


def showStatistics():
    print("Min: {}".format(minimum))
    print("Max: {}".format(maximum))
    print("Average: {}".format(average))


getChoice()
