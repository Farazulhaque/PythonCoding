print("Answer by only typing [Y/n]")
uncompressed = input(
    "Assignment submitted as a single uncompressed .py file? ").lower()
namedate = input("Assignment include the author's name and date? ").lower()
if namedate == "n":
    exit(0)
honorstmt = input("Assignment include honor statement? ").lower()
video = input("Assignment include 3-minute video? ").lower()

grade = 0
if uncompressed == "y" and namedate == "y" and honorstmt == "y" and video == "y":
    grade += int(input("Out of 10 points, how would you evaluate the correctness of the code? "))
    grade += int(input("Out of 10 points, how would you evaluate the elegance of the code? "))
    grade += int(input("Out of 10 points, how would you evaluate the code hygiene? "))
    grade += int(input("Out of 10 points, how would you evaluate the quality of discussion? "))
    late = input("Is assignment late subitted? ").lower()
    if late == "y":
        time = int(input("How late it is? "))
        grade = grade - (grade * time/100)
    print("\nTotal grade :", grade)
else:
    print("\nTotal grade :", grade)
