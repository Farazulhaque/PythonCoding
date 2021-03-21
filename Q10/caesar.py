message = input("Secret message: ")
shift = int(input("Shift: "))
length = len(message)  # get length of the message
encrypt = ""  # get empty string to store encrypted message
for i in range(length):
    # ord('a) is used to get the integer/ASCII value of a character so that we can compare if it is alphabet or not.
    if (ord(message[i]) >= ord('a') and ord(message[i]) <= ord('z')):
        encrypt = (((ord(message[i]) - ord('a')) + shift) % 26) + ord('a')
        # ord(message[i]) will get the integer value of a character
        # ord('a') will get the integer value of a
        # we have to subtract ord('a') from ord(message[i]) so that every letter matches its order
        # i.e a=0,b=1,c=2 and so on
        # now we have to add the value of shift variable
        # now we have to mod by 26 so that we get the shift digit letter
        # now to get that letter, we have to add again value of ord('a')
        # this if for lower case letter
        # similar rule is applied for upper case alphabets below
        print(chr(encrypt), end="")
    elif (ord(message[i]) >= ord('A') and ord(message[i]) <= ord('Z')):
        encrypt = (((ord(message[i]) - ord('A')) + shift) % 26) + ord('A')
        print(chr(encrypt), end="")
    else:
        print(message[i], end="")  # if it is not alphabet print as it is
