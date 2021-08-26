# read data
with open("coordinates.txt", "r") as f:
    coordinates = [line.strip().split(";") for line in f.readlines()]

coordinates = sorted(coordinates, key=lambda x: int(x[0][1:]))

# now write data into points.txt file
with open("points.txt", "w") as f:
    f.write("%s%12s%15s%16s" % ("ID", "East", "North", "Height"))
    f.write("\n")
    f.write("-"*5+"|"+"-"*13+"|"+"-"*15+"|"+"-"*10)
    f.write("\n")
    for eachLine in coordinates:
        for data in range(len(eachLine)):
            if data == 0:
                f.write(eachLine[data])
            elif data == 3:
                f.write("%9s" % str(round(float(eachLine[data]), 2)))
            else:
                f.write("%13s" % (str(round(float(eachLine[data]), 2))))
            f.write("\t")
        f.write("\n")

# calulate stats
heights = []
for h in coordinates:
    heights.append(float(h[-1]))

average = sum(heights)/len(heights)
maximum = max(heights)
minimum = min(heights)
difference = maximum - average

# writing stats into file stat.txt
with open("stat.txt", "w") as f:
    f.write(f"Average height of the points are {average:.2f}\n")
    f.write(f"Maximum height is {maximum:.2f}\n")
    f.write(f"Minimum height is {minimum:.2f}\n")
    f.write(
        f"Difference between maximum height and average height is {difference:.2f}\n")
