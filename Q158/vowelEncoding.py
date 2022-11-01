#Intro
def main():
	string=input("Enter a sentence:")
	print("The new sentence is:",end=' ')
	EncodeString(string)

def EncodeString(string):
	encodedString = ""
	for i in string:
		encodedString += EncodeCharacter(i)

	print(encodedString)

def EncodeCharacter(i):
	#Start with the capital vowel
	if i == 'A':
		return 'E'
	elif i == 'E':
		return 'I'
	elif i == 'I':
		return 'O'
	elif i == 'O':
		return 'U'
	elif i == 'U':
		return 'A'
	
	#Then, the lower vowel
	elif i == 'a':
		return 'e'
	elif i == 'e':
		return 'i'
	elif i == 'i':
		return 'o'
	elif i == 'o':
		return 'u'
	elif i == 'u':
		return 'a'

	#printing other letters in the sentence as it is
	else:
		return i
	
main()

