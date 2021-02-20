import re

# Make a regular expression for validating an Email
regex = '^[a-zA-Z][\w]*@[\w]+\.[\w]+$'
# ^[a-zA-z] this is used to check for start with letters a-zA-z
# [\w] is used to check it contains a-zA-z0-9 or not
# * for zero or more number of times \w
# @ this is used to check the third rule i.e followed by @
# [\w] is used to check it contains a-zA-z0-9 or not
# +\. followed by a period
# [\w] followed by a string that contain one or more letter or numbers
# $ is used in regular expression to check for end condition


# Define a function for validating an Email
def check(email):
    # pass the regular expression and the string in search() method
    if(re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Enter the email
email = "x@8.7"
check(email)

email = "1abc@yahoo.com"  # invalid, as begins with a letter
check(email)

email = "a14b@test1.com1"
check(email)
