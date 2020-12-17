word = input("Enter simple password: ")
password = ''
for i in range(len(word)):  # loop over the word
    if 'i' in word[i]:  # check if a letter i is in word or not
        password += '!'  # if condition is true replace ! to password variable
    elif 'a' in word[i]:
        password += '@'
    elif 'm' in word[i]:
        password += 'M'
    elif 'B' in word[i]:
        password += '8'
    elif 'o' in word[i]:
        password += '.'
    else:
        # if no condition is true then the letter in word is copied to password variable
        password += word[i]
password += 'q*s'  # add 'q*s' at the end of the value stord in password variable
print("Your strong password is: "+password)
