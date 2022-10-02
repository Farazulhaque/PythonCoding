# Show the user prices for each delivery option
print("The delivery option and there prices are: ")
print("1. Express Delivery: 40 AED")
print("2. Standard Delivery: 25 AED")
print("3. Premium Delivery: 60 AED")
# defining variable for delivery prices
express = 40
standard=25
premium=60
# taking input for delivery option and package weight
delivery_option = int(input("Enter a delivery option: "))
package_weight = float(input("Enter b to enter the weight of the package: "))
# To calculate the total cost of delivery
cost = 0
# if delivery option is express
if(delivery_option == 1):
	if(package_weight > 3):
		cost = express + 15
	else:
		cost = express
# if delivery option is standard
elif (delivery_option == 2):
	if(package_weight > 3):
		cost = standard + 10
	else:
		cost = standard
# if delivery option is premium
elif (delivery_option == 3):
	if(package_weight > 3):
		cost = premium + 25
	else:
		cost = premium
else:
	print("Incorrect delivery option.")

# Show the cost of delivery
print("The total cost of delivery is " + str(cost) + " AED")
