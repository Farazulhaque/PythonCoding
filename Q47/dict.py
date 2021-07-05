students = {'Sally': ['B', 3, 'A', 3, 'A', 4, 'D', 2], 'John': [
    'C', 3, 'D', 1, 'A', 2, 'A', 1], 'Mike': ['A', 3, 'C', 2], 'Ron': ['B', 4]}
letters = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

names = list(students.keys())
grades = list(students.values())


# to store student names and weighted GPAs
dic = {}

# Loop over list of grades of each student
for i in range(len(grades)):
    # for calculating total credit of each student
    total = 0
    credit = 0
    # For checking grades of students if it contains A, B, C, D, F
    for j in range(len(grades[i])):
        if grades[i][j] in ['A', 'B', 'C', 'D', 'F']:
            total += (letters.get(grades[i][j]) * grades[i][j + 1])
            credit += grades[i][j + 1]
        weighted_gpa = total / credit
        # ADD TO DICT STUDENT NAME AND WEIGHTED GPAs
        dic[names[i]] = round(weighted_gpa, 2)
print(dic)
