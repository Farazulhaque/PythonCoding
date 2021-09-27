def fahrenheit(celsius):
    return (9 / 5) * celsius + 32


def main():
    print("%8s %12s" % ("Celsius", "Fahrenheit"))
    for i in range(101):
        C = i
        F = fahrenheit(C)
        print("%6s %3s %6s" % ("{:.1f}".format(C), ":", "{:.1f}".format(F)))


main()
