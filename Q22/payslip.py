item_name = input("Item Name: ")

item_price = int(input("Item Price: "))
while item_price < 0:
    item_price = int(input("Item Price: "))
    
item_quantity = int(input("Item Quantity: "))
while item_quantity < 0:
    item_quantity = int(input("Item Quantity: "))

total_amount = item_quantity * item_price
if total_amount > 500:
    total_amount = total_amount - total_amount/10
elif total_amount >= 299 and total_amount <= 499:
    total_amount = total_amount - total_amount/5
else:
    total_amount = total_amount

print("\nItem Name    :", item_name)
print("Total Amount : ${:.2f}".format(total_amount))
