# Getting user input separated by space
l1 = input().split()
# Create empty list
quarterly_sales = []
# Loop in user input
for i in l1:
    try:
        # append in quarterly_sales if the data inputted by user is number
        quarterly_sales.append(int(i))
    except:
        print("All sales should be numeric")

# Check for correct quarters
if len(quarterly_sales) == 4:
    # use sum function to get sum of quarterly_sales
    total_sales = sum(quarterly_sales)
    # by using end="", it will print the next statement in same line
    print("Quarterly sales: $", end="")
    # Python3 has sep parameter to print the content separated by ", "
    # * is used to print all the elements in the quarterly_sales
    print(*quarterly_sales, sep=", $")
    if(total_sales < 50000):
        print("Sales: low")
    elif (total_sales >= 50000 or total_sales < 150000):
        print("Sales: med")
    elif (total_sales >= 150000):
        print("Sales: high")
    if(total_sales < 20000):
        print("Warning: Need to improve sales")
