# Getting user input
A = float(input("Enter a deposit amount: "))
W = float(input("Enter interest rate: "))
N = int(input("Enter period: "))
# initialise values to 0, Use it in later part
totalDeposits = 0
totalInterest = 0
toDate = 0
print(
    f"\nTHE OF INTEREST MADE BY AN INVESTMENT OF ${A} EVERY MONTH AT AN INTEREST RATE OF {W}% FOR {N} MONTHS\n")
# printing header
print("%5s %15s %20s %25s %25s" % ("Month", "Deposit", "Total Deposits",
      "This Month's interest", "Total-Interest Earned"))
print("%27s" % ("Total-Value To-Date"))
# printing data
for month in range(1, N+1):
    # As per formula calculate amount of money accumulated after N months
    F = A*(1+W/1200)**month
    # Add amount to total deposit on each iteration
    totalDeposits += A
    # Add F to todate value on each iteration
    toDate += F
    # calculae interest
    interest = F - A
    # calculate total interest
    totalInterest += interest
    # printing data
    print("%5s %15s %15s %15s %25s" % ("{0:.2f}".format(
        month), A, totalDeposits, "{0:.2f}".format(interest), "{0:.2f}".format(totalInterest)))
    print("%20s" % ("{0:.2f}".format(F)))
