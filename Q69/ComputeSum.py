def compute_sum(filename):
    try:
        infile = open(filename, "r")
        sums = 0
        count = 0
        for line in infile:
            line = line.strip()
            num = float(line)
            if num % 2 != 0:
                sums += num
                count += 1

        print("Sum of the odd numbers is: {:.2f}".format(sums))
        print("Average is: {:.2f}".format(sums/count))
    except:
        print("ERROR: File can't open")


compute_sum("sumdata.txt")
