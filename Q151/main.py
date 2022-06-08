def main():
	nums = []
	while True:
		n = int(input())
		try:
			if n == 0:
				break
			elif n >= 0 and n <= 100:
				nums.append(n)
			else:
				n = int(input())
		except:
			print("exception catched")

	avg = sum(nums)/2
	print(sum(nums))
	print(avg)

main()