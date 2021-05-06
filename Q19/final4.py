import sys


def myaverage(last_name, class1_grade, class2_grade, class3_grade, class4_grade):
    grade = [class1_grade, class2_grade, class3_grade, class4_grade]
    marks = []
    total = 0
    for i in range(len(grade)):
        if grade[i] == "A":
            marks.append(4)
        elif grade[i] == "B":
            marks.append(3)
        elif grade[i] == "C":
            marks.append(2)
        else:
            marks.append(0)
    for i in range(len(marks)):
        if marks[i] == 0:
            print(last_name, ", You should complete 4 courses to have your GPA calculated ")
            return 0
        else:
            total += marks[i]
            gpa = total / 4
    print(last_name, ", Your semester GPA is ", gpa)


if len(sys.argv) > 1:
    l1 = sys.argv[1]
    newlist = l1.split(",")
    last_name = newlist[0]
    first_name = newlist[1]
    class1_grade = newlist[2]
    class2_grade = newlist[3]
    class3_grade = newlist[4]
    class4_grade = newlist[5]
    myaverage(last_name, class1_grade, class2_grade,
              class3_grade, class4_grade)

else:
    print("Usage: python final4.py lastname,firstname,class1grade,class2grade,class3grade,class4grade,")
