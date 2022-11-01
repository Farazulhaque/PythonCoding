# variables to store count
uppercase = 0
lowercase = 0
digits = 0
space = 0
words_per_line = []

# reading file
with open('Story.txt', 'r') as file:
	# reading line by line
	for line in file:
		# reading each character
		for char in line:
			if char.isupper():
				uppercase += 1
			elif char.islower():
				lowercase += 1
			elif char.isdigit():
				digits += 1
			elif char.isspace():
				space += 1
		# storing words per ine in an array
		words_per_line.append(len(line.split(" ")))

# printing output
print("Amount of Uppercase letters: ", uppercase)
print("Amount of Lowercase letters: ",lowercase)
print("Amount of Digits: ",digits)
print("Amount of Spaces: ",space)
print("Average number of words per line:",round(sum(words_per_line)/len(words_per_line), 2))

