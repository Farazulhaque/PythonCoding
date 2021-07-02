global username, major, birthday, percent


def name():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    return first_name + " " + last_name


def majr():
    major = input("Enter major: ")
    return major


def bday():
    month = int(input("What is your birth month? "))
    day = int(input("What is your day of birth? "))
    year = int(input("What is your birth year? "))
    birthday = str(month) + "/" + str(day) + "/" + str(year)
    return birthday


def courseTaken(classes_taken, classes_remaining):
    total_classes = classes_taken + classes_remaining
    return classes_taken / total_classes * 100


def classes():
    classes_taken = int(
        input("How many classes have you're taken in college? "))
    classes_remaining = int(input("How many classes do you have remaining? "))
    course_taken_percentage = courseTaken(classes_taken, classes_remaining)
    return course_taken_percentage


def main(username, major, birthday, percent):
    print("Name: {}".format(username))
    print("Major: {}".format(major))
    print("Birthday: {}".format(birthday))
    print("Course Completion Percentage: {}".format(percent))


username = name()
major = majr()
birthday = bday()
percent = classes()
main(username, major, birthday, percent)

cont = True
while cont == True:
    print("a)Update Name\nb)Update Major\nc)Update Birthday\nd)Update Course Information\ne)Display Information")
    choice = input("Enter your choice:(a,b,c,d,e) ")

    if choice.lower() == "a":
        username = name()
    elif choice.lower() == "b":
        major = majr()
    elif choice.lower() == "c":
        birthday = bday()
    elif choice.lower() == "d":
        percent = classes()
    elif choice.lower() == "e":
        main(username, major, birthday, percent)

    answer = input("Would you like to continue?(yes/no) ")
    if(answer.lower() == "no"):
        cont = False
