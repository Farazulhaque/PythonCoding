horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

print("Vowels in horton in the order they appear in horton are: ", end = "")
# loop in hortom string
for letter in horton:
    # check each letter in vowels string
    # if in vowels then print it
    if letter in vowels:
        print(letter, end="")


