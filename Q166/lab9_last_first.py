def readFile(filename):
	dict = {}
	with open(filename) as file:
		for line in file:
			for char in line:
				if char.isalpha():
					if char.lower() in dict.keys():
						dict[char.lower()] += 1
					else:
						dict[char.lower()] = 1
	return dict


def sortKeys(dict):
	lst = list(dict.keys())
	return sorted(lst)

def main():
	dict = readFile("speech.txt")
	keys = sortKeys(dict)

	print("The frequency of letters are: ")
	for letter in keys:
		print(f"{letter} : {dict[letter]}")


main()



