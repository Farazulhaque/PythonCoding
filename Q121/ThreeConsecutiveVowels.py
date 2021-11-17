word = input("Enter a string: ")
# to store new word
new = ""
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

i = 0
# loop until last index
while (i < len(word)):
    # if i less than length of word - 2
    # because 3 consecutive vowels
    if (i < len(word)-2):
        # check if vowels or not
        if word[i] in vowels:
            if word[i+1] in vowels:
                if word[i+2] in vowels:
                    # then add 3 #
                    new += "###"
                    # and set i = i + 2
                    i += 2
                # else add same letter to new variable
                else:
                    new += word[i]
            # else add same letter to new variable
            else:
                new += word[i]
        # else add same letter to new variable
        else:
            new += word[i]
    # else add same letter to new variable
    else:
        new += word[i]
    # increment i on each iteration
    i += 1
print(new)
