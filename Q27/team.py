from builtins import max

team_name = input("Enter the name of your Team: ")
foundation_year = int(input("Enter the foundation year: "))
if foundation_year > 1920:
    d = {}
    for i in range(foundation_year, 2021):
        trophy = int(input("Enter the number of titles won in %d : " % i))
        while trophy < 0:
            trophy = int(input("Enter the number of titles won in %d : " % i))
        d[i] = trophy
    total_year = 2020 - foundation_year
    trophies = d.values()
    total_trophy = sum(trophies)
    avg = total_trophy / total_year
    print("The average of titles won is", int(avg))
    best_season = max(d, key=d.get)
    max = d.get(best_season)
    print("The best season was in {}. {} won {} titles".format(
        best_season, team_name, max))
else:
    print("Invalid Input!")


