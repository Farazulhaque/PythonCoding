def Netsal(Sal):
    for salaries in range(len(Sal)):
        if Sal[salaries] < 2000:
            Sal[salaries] += 300
        elif Sal[salaries] >= 4000:
            Sal[salaries] += 100
        else:
            Sal[salaries] += 200
    return Sal


def main():
    Record = [["Ali", "Mazen", "Fida", "Nader", "Majid"],
              ["Tutor", "IT", "Manager", "PR", "Clerk"]]
    Sal = [2200, 1600, 4000, 2000, 1400]
    Netsal(Sal)
    for i in range(len(Sal)):
        print(Record[0][i], "-", Record[1][i], ":", Sal[i])


main()
