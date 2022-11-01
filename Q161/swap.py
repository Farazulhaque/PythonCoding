def swap_values(user_val1, user_val2, user_val3, user_val4):
	temp = user_val1
	user_val1 = user_val2
	user_val2 = temp
	temp = user_val3
	user_val3 = user_val4
	user_val4 = temp
	print(f"{user_val1} {user_val2} {user_val3} {user_val4}")

if __name__ == '__main__':
	user_val1 = int(input())
	user_val2 = int(input())
	user_val3 = int(input())
	user_val4 = int(input())
	swap_values(user_val1, user_val2, user_val3, user_val4)
