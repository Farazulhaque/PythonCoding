def main():
	# to store list of unique words
	words = []

	# reading file
	with open('TongueTwister.txt', 'r') as file:
		# reading line by line
		for line in file:
			# split line by space to get each word
			for word in line.split(" "):
				# check word is in words list or not
				if "".join(word.rsplit()) not in words:
					words.append("".join(word.rsplit()))


	# print the sorted list of words 
	for ele in sorted(words):
		print(ele)

main()

