def main():
    cans = [248, 379, 189, 457, 274, 532, 279, 296, 359]
    total = totalCans(cans)
    average = total / len(cans)
    print(f"Total number of cans collected are {total}")
    print(f"Average number of cans collected are {average}")
    above_average = aboveAverage(cans, average)
    highest_grade = highest(cans)
    print(
        f"The grade with the highest number of cans collected is {highest_grade}")
    lowerst_grade = lowest(cans)
    print(
        f"The grade with the lowest number of cans collected is {lowerst_grade}")


def totalCans(cans):
    total = 0
    for i in cans:
        total += i
    return total


def aboveAverage(cans, average):
    above_average = 0
    for i in cans:
        if i > average:
            above_average += 1
    print(
        f"Number of classrooms that collectec above the average are {above_average}")


def highest(cans):
    grade = 0
    max = cans[0]
    for i in range(1, len(cans)):
        if max < cans[i]:
            max = cans[i]
            grade = i
    return grade


def lowest(cans):
    grade = 0
    min = cans[0]
    for i in range(1, len(cans)):
        if min > cans[i]:
            min = cans[i]
            grade = i
    return grade


main()
