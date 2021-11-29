def main():
    file_students = open("Q133\student_points.txt", "r")
    stu_name = file_students.readline()  # read the first record,
    # which is the first stduent's name
    num_stu = 0

    print(f"Student              Points    Grade")
    print("-------------------------------------\n")
    stu_failed = 0
    while stu_name != "":
        stu_name = stu_name.rstrip("\n")  # strip \n from name
        stu_points = file_students.readline()  # read numeric points
        stu_points = int(stu_points)  # cast points into an int

        if (stu_points < 60):
            print(f"{stu_name:15}        {stu_points}      **F**")
            stu_failed += 1
        else:
            print(f"{stu_name:15}        {stu_points}")

        num_stu += 1

        stu_name = file_students.readline()

    file_students.close()
    print()
    print(f"Number of students processed = {num_stu}")
    print(f"Number of 'F' students       = {stu_failed}")
    stu_passed = "{:.1f}".format((num_stu - stu_failed) * 100 / num_stu)
    print(f"% of students who passed     = {stu_passed}%")


main()
