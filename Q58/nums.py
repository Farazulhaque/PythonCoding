def main():
    # Create empty list to store numbers
    nums = []
    # To loop untill user enter -ve number
    addnums = True
    while addnums == True:
        # Get user input
        num = int(input("Enter numbers: "))
        # If positive
        if num >= 0:
            # Add number to list nums
            nums.append(num)
        else:
            addnums = False

    # in-built functions to get minimum, maximum and sum of numbers
    lowest = min(nums)
    highest = max(nums)
    total = sum(nums)
    # Divide total by length of list to get average
    average = total / len(nums)
    # Printing
    print(f"Lowest = {lowest}")
    print(f"Highest = {highest}")
    print(f"Average = {average}")


# Calling main()
main()
