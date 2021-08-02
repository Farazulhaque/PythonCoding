list1 = [1, 0, 8, 3, 8, 8, 1]
# largest number in the list
largest = max(list1)
print(f"Largest number in the list is {largest}")
# smallest number in the list
smallest = min(list1)
print(f"Smallest number in the list is {smallest}")
# second largest number in the list
list1 = set(list1)
list1.remove(largest)
secondLargest = max(list1)
print(f"Second largest number in the list is {secondLargest}")

list2 = ['Z', 'a', 'y', 'e', 'd', ' ', 'A', 'l',
         'm', 'u', 'h', 'a', 'i', 'r', 'i', 'b', 'i']

list3 = []

for ele in list1:
    list3.append(ele)
for ele in list2:
    list3.append(ele)

print(f"All items of list1 and list2 are {list3}")
