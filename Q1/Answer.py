def cal_factorial(n):
    if n == 1:
        return n
    else:
        return n*cal_factorial(n-1)
# -------------------------------------------------------


def list_multiples(number, length):
    a = range(number, (length * number)+1, number)
    result = list(a)
    print(result)
# -------------------------------------------------------


def find_max(a_list):
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = a_list[0]

    # Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in a_list:
        if x > max:
            max = x

    # after complete traversing the list
    # return the "max" value
    return max
