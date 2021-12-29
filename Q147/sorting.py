from datetime import datetime


def readFile(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    # print(numbers)
    return numbers

def insertionSort(arr):
    for i in range(1, len(arr)):
 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


filename = "numbers10.dat"
nums = readFile(filename)
init_time = datetime.now()
insertionSort(nums)
fin_time = datetime.now()
print(f"Execution time (insertionSort) : {filename} {str((fin_time-init_time))[5:]}")

filename = "numbers100.dat"
nums = readFile(filename)
init_time = datetime.now()
insertionSort(nums)
fin_time = datetime.now()
print(f"Execution time (insertionSort) : {filename} {str((fin_time-init_time))[5:]}")

filename = "numbers1000.dat"
nums = readFile(filename)
init_time = datetime.now()
insertionSort(nums)
fin_time = datetime.now()
print(f"Execution time (insertionSort) : {filename} {str((fin_time-init_time))[5:]}")

filename = "numbers10000.dat"
nums = readFile(filename)
init_time = datetime.now()
insertionSort(nums)
fin_time = datetime.now()
print(f"Execution time (insertionSort) : {filename} {str((fin_time-init_time))[5:]}")

filename = "numbers100000.dat"
nums = readFile(filename)
init_time = datetime.now()
insertionSort(nums)
fin_time = datetime.now()
print(f"Execution time (insertionSort) : {filename} {str((fin_time-init_time))[5:]}")

filename = "numbers1000000.dat"
nums = readFile(filename)
init_time = datetime.now()
insertionSort(nums)
fin_time = datetime.now()
print(f"Execution time (insertionSort) : {filename} {str((fin_time-init_time))[5:]}")
