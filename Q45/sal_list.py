count = int(input("Enter number of employees: "))
basic_salary = []
year_of_exp = []
bonus = []
gross_salary = []
total_salary = 0
employees_sal_gt_2000 = 0
for i in range(1, count+1):
    sal = int(input(f"Enter basic salary of employee {i}: "))
    exp = int(input(f"Enter year of exprn of employee {i}: "))
    basic_salary.append(sal)
    year_of_exp.append(exp)
    if exp <= 20:
        if sal < 1000:
            bons = (sal/100) * 1
        elif sal >= 100 and sal < 1500:
            bons = (sal/100) * 2
        elif sal >= 1500 and sal < 2000:
            bons = (sal/100) * 3
        elif sal > 2000:
            bons = (sal/100) * 5
            employees_sal_gt_2000 += 1
    else:
        bons = (sal/100) * 7
    gross_sal = sal + bons
    bonus.append(bons)
    gross_salary.append(gross_sal)
    total_salary += gross_sal
print("\nBasic Salary\tBonus\tGross Salary")
for i in range(count):
    print("{:.2f} \t{:.2f}\t{:.2f}".format(
        basic_salary[i], bonus[i], gross_salary[i]))

print("\nAverage Gross Salary is......................:", total_salary/count)
print("Number of employees whose basic salary > 2000:", employees_sal_gt_2000)
