def exact_change(cents):
	quarters = int(cents/25)
	cents = cents - (quarters*25)
	dimes = int(cents/10)
	cents = cents - (dimes*10)
	nickels = int(cents/5)
	cents = cents - (nickels*5)
	pennies = cents
	
	return quarters, dimes, nickels, pennies


if __name__ == '__main__':
	input_val = int(input())
	
	if(input_val == 0):
		print("no change")

	num_quarters, num_dimes, num_nickels, num_pennies  = exact_change(input_val)

	if num_dimes == 1:
		print(f"{num_dimes} Dime", end="\n")
	elif num_dimes > 1:
		print(f"{num_dimes} Dimes", end="\n")

	if num_quarters == 1:
		print(f"{num_quarters} quarter", end="\n")
	elif num_quarters > 1:
		print(f"{num_quarters} quarters", end="\n")
    
	if num_nickels == 1:
		print(f"{num_nickels} Nickel", end="\n")
	elif num_nickels > 1:
		print(f"{num_nickels} Nickels", end="\n")

	if num_pennies == 1:
		print(f"{num_pennies} Penny", end="\n")
	elif num_pennies > 1:
		print(f"{num_pennies} Pennies", end="\n")

