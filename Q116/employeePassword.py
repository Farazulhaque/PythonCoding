import string
import random
import csv


# to read and store csv file content into list
fname = []
lname = []
phone = []
email = []
paswd = []

# count total employees
count = 0
with open("employee.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        fname.append(row[0])
        lname.append(row[1])
        phone.append(row[2])
        email.append(row[3])
        count += 1


# Length of the generated password
PASS_LENGTH = 16

# Number of passwords to generate
NUM_PASS = count


# Generate a password of size length using all ascii letters, numbers 0-9
# and a subset of special characters
def gen_pass(length):
    all = string.ascii_letters + string.digits + '!@#$%^&*()-_+=~[]{};<>?/\|'
    password = "".join(random.sample(all, length))
    return password


i = 0
while i < NUM_PASS:
    paswd.append(gen_pass(PASS_LENGTH))
    i += 1


# print(fname)
# print(lname)
# print(phone)
# print(email)
# print(paswd)

# write password to a csv file
with open('new_employee.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['fname', 'lname', 'phone', 'email', 'password'])
    for i in range(count):
        writer.writerow([fname[i], lname[i], phone[i], email[i], paswd[i]])
