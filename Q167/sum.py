num = int(input("Enter a number: "))
sum = 0
while(num!=0):
	n = num%10
	num = int(num/10)
	sum += n

print(f"Sum of all digits is {sum}")
if(sum < 10):
	print("Below 10.")
elif(sum < 20):
	print("Between 10 and 20.")
else:
	print("Greater than 20.")