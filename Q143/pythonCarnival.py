import random

print("Welcome to the Python Carnival Games! \
        Our program will ask you a series of questions \
        and use your answers to guess different things about you.")

print("The first game will use some questions to determine your birthday. \
    These questions will be easy to answer as long as you know your birthday!")

# first game: birthday
ticket_count = 0
guesscount = 0
birthday = random.randint(1, 31)
while(guesscount < 15):
    print(f"Your birthday is {birthday}")
    is_correct = input("Is it correct?[Y/n] ").lower()
    if is_correct == 'y':
        break
    else:
        print(f"Your birthdate is greater than {birthday}?[Y/n] ", end="")
        q = input()
        if q == "y":
            birthday = random.randint(birthday, 31)
        else:
            birthday = random.randint(1, birthday)
        guesscount += 1

if is_correct == 'y':
    ticket_count += 1
else:
    print("You lose")

# second game: weight
guesscount = 0
weight = random.randint(1, 31)
while(guesscount < 15):
    print(f"Your weight is {weight}")
    is_correct = input("Is it correct?[Y/n] ").lower()
    if is_correct == 'y':
        break
    else:
        print(f"Your weight is greater than {weight}?[Y/n] ", end="")
        q = input()
        if q == "y":
            weight = random.randint(weight, 31)
        else:
            weight = random.randint(1, weight)
        guesscount += 1

if is_correct == 'y':
    ticket_count += 1
else:
    print("You lose")

# second game: height
guesscount = 0
height = random.randint(1, 31)
while(guesscount < 15):
    print(f"Your height is {height}")
    is_correct = input("Is it correct?[Y/n] ").lower()
    if is_correct == 'y':
        break
    else:
        print(f"Your height is greater than {height}?[Y/n] ", end="")
        q = input()
        if q == "y":
            height = random.randint(height, 31)
        else:
            height = random.randint(1, height)
        guesscount += 1

if is_correct == 'y':
    ticket_count += 1
else:
    print("You lose")


if ticket_count > 0:
    print(f"You got {ticket_count}! Great Job!")

else:
    print("You didn't get any tickets, sorry!")
