sentence = input("Enter a sentence: ")
print("Indexes of characters that are not vowels: ")
# Loop in the range of length of sentence string 
for i in range(len(sentence)):
    # First convert the character at sentence[i] into lower case
    # then check if it is in ['a','e','i','o','u']. If yes 
    # then don't print and if it is not present in this then print it
    # as in condition we have write 'not in'
    if sentence[i].lower() not in ['a','e','i','o','u']:
        print(i, end = " ")