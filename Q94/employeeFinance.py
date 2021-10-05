import csv
from os import read

emp_name = []
gender = []
position_title = []
position_num = []
exp = []
performance = []
records = 0


def print_menu():
    print("\nEnter 1 to print record of an employee")
    print("Enter 2 to get number of records stored in the file")
    print("To print all records")
    print("\tEnter a to print Employee Name, Position #, Experience")
    print("\tEnter b to print Employee Name and Position Title")
    print("\tEnter c to print Employee name and performance in 2021")
    print("Enter 4 to add a record")
    print("Enter 5 to quit")


def main():
    while 1:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name of an employee: ")
            for i in range(len(emp_name)):
                if name.lower() == emp_name[i].lower():
                    print(f"Employee Name: {emp_name[i]}")
                    print(f"Gender: {gender[i]}")
                    print(f"Position Title: {position_title[i]}")
                    print(f"Position Num: {position_num[i]}")
                    print(f"Experience: {exp[i]}")
                    print(f"Performance in the year 2021: {performance[i]}")

        elif choice == "2":
            print(f"Total records stored in a file are: {records-1}")

        elif choice == "a":
            print("Employeee Name\tPosition #\tExperience")
            for i in range(len(emp_name)):
                print(f"{emp_name[i]}\t{position_num[i]}\t{exp[i]}")

        elif choice == "b":
            print("Employeee Name\tPosition Title")
            for i in range(len(emp_name)):
                print(f"{emp_name[i]}\t{position_title[i]}")

        elif choice == "c":
            print("Employeee Name\tPerformance in 2021")
            for i in range(len(emp_name)):
                print(f"{emp_name[i]}\t{performance[i]}")

        elif choice == "5":
            exit()

        else:
            print("Invalid input...")


with open('Employee_Finance.csv', 'r') as Employee_Finance:
    reader = csv.reader(Employee_Finance)
    # print(reader)
    for row in reader:
        records += 1
        if records != 1:
            emp_name.append(row[0])
            gender.append(row[1])
            position_title.append(row[2])
            position_num.append(row[3])
            exp.append(row[4])
            performance.append(row[5])


main()
