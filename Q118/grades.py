def main():
    print("Welcome to Letter Grade Counter Program!")
    print("-"*40)
    gradeBook = fillGradeBook()
    print("-"*40)

    # print(gradeBook)
    # exit(0)

    count = countGrades(gradeBook)
    gradeReport(count)


def fillGradeBook():
    gradeBook = {}
    count = int(input("How many grades do you want to enter? "))
    for i in range(count):
        print(f"Enter the name of student #{i+1}: ", end="")
        name = input()
        print(f"What is {name}'s grade? ", end="")
        grade = input().upper()
        gradeBook[name] = grade

    return gradeBook


def countGrades(gradeBook):
    grades = ['A', 'B', 'C', 'D', 'F']
    g = []
    count = []
    for grade in gradeBook:
        g.append(gradeBook[grade])
    for i in grades:
        count.append(g.count(i))

    return count


def gradeReport(count):
    grades = ['A', 'B', 'C', 'D', 'F']
    print(f"Grade\tCount")
    print("-"*40)
    for i in range(len(grades)):
        print("%-10s %-10s" % (grades[i], count[i]))


main()
