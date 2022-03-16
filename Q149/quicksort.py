import time

def partition(list_of_items, first, last, pivot_index):
    """Moves the pivot to correct index in the list"""
    if pivot_index == 1:
        pivot_value = list_of_items[0]
    else:
        midpoint = len(list_of_items) // 2
        pivot_value = list_of_items[midpoint]
        list_of_items[0], list_of_items[midpoint] = list_of_items[midpoint], list_of_items[0]
    left_index = first
    right_index = last
    while left_index < right_index:
        while list_of_items[left_index] < pivot_value:
            left_index += 1
        while left_index <= right_index and list_of_items[right_index] >= pivot_value:
            right_index -= 1
        if left_index < right_index:
            list_of_items[left_index], list_of_items[right_index] = list_of_items[right_index], list_of_items[left_index]
    list_of_items[right_index], list_of_items[0] = list_of_items[0], list_of_items[right_index]

    return right_index


def realQuickSort(list_of_items, first, last, pivot_index):
    """Does the actual quick sort in items in list in ascending order"""
    if len(list_of_items) == 1:
        return list_of_items
    partition_index = partition(list_of_items, first, last, pivot_index)
    partition(list_of_items, first, partition_index - 1, pivot_index)
    partition(list_of_items, partition_index + 1, last, pivot_index)


def quickSort(list_of_items, pivot_to_use='first'):
    """Do a quick sort on items in list_of_items in ascending order and return sorted list and elaspsed_time"""
    start_time = time.time()

    max = len(list_of_items)-1
    if pivot_to_use == 'first':
        pivot_index = 1
        realQuickSort(list_of_items, 0, max, pivot_index)
    else:
        pivot_index = 2
        realQuickSort(list_of_items, 0, max, pivot_index)

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


list = [8, 45, 24, 17, 6, 84, 68, 2]
list2 = [8, 45, 24, 17, 6, 84, 68, 2]
print(list)
print(quickSort(list, 'first'))
print(list2)
print(quickSort(list, 'middle'))