numbers = []
names = []
surnames = []
birtplaces = []
departments = []
gpas = []

with open("students.dat", "r") as file:
    next(file)
    next(file)
    for line in file:
        data = line.split()
        numbers.append(int(data[0]))
        names.append(data[1])
        surnames.append(data[2])
        birtplaces.append(data[3])
        departments.append(data[4])
        gpas.append(float(data[5]))


def print_name(student_number):
    i = numbers.index(student_number)
    print(names[i])


def print_surname(student_number):
    i = numbers.index(student_number)
    print(surnames[i])


def print_birth_place(student_number):
    i = numbers.index(student_number)
    print(birtplaces[i])


def print_department(student_number):
    i = numbers.index(student_number)
    print(departments[i])


def print_gpa(student_number):
    i = numbers.index(student_number)
    print(gpas[i])


print_name(13726146)
print_surname(13726146)
print_birth_place(13726146)
print_department(13726146)
print_gpa(13726146)
