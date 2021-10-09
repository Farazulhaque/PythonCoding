# initialising prizes
small = 10
medium = 12
large = 15
meat = 2
veggie = 1
combo = 3
original = 0
handTossed = 1
crispy = 1.50
stuffed = 3

total = 0
print("Build your pizza!")
size = input(
    "\nWe have [S]mall, [M]edium, [L]arge pizza, which size do you prefer? ")
while size.upper() not in ['S', 'M', 'L']:
    size = input(
        "Your pizza is only available in size [S]mall, [M]edium or [L]arge: ")

s = ""
sizePrice = 0
if size.upper() == "L":
    s = "large"
    sizePrice = large
    total += large
elif size.upper() == "M":
    s = "medium"
    sizePrice = medium
    total += medium
elif size.upper() == "S":
    s = "small"
    sizePrice = small
    total += small

print(f"You have chosen a {s} pizza.")

toppings = input(
    "\nWould you like [M]eat toppings, [V]eggie toppings or [C]ombo toppings with both meat and veggie? ")
while toppings.upper() not in ['M', 'V', 'C']:
    toppings = input(
        "Please enter your what toppings you would like to order, [M]eat, [V]eggie or [C]ombo: ")

t = ""
toppingPrice = 0
if toppings.upper() == "M":
    t = "meat"
    toppingPrice = meat
    total += meat
elif toppings.upper() == "V":
    t = "veggie"
    toppingPrice = veggie
    total += veggie
elif toppings.upper() == "C":
    t = "combo"
    toppingPrice = combo
    total += combo

print(f"You have chosen a {s} {t} pizza.")

if toppings.upper() == 'M':
    crust = input("\nWould you like [O]riginal Crust or [S]tuffed Crust? ")
    c = ""
    crustPrice = 0
    while crust.upper() not in ['O', 'S']:
        crust = input(
            "Please enter your crust preference, [O]riginal Crust or [S]tuffed Crust: ")
    if crust.upper() == "O":
        total += original
        crustPrice = original
        c = "original"
    elif crust.upper() == 'S':
        total += stuffed
        crustPrice = stuffed
        c = "stuffed"

elif toppings.upper() == 'V':
    crust = input("\nWould you like [O]riginal Crust or [C]rispy Crust? ")
    c = ""
    crustPrice = 0
    while crust.upper() not in ['O', 'C']:
        crust = input(
            "Please enter your crust preference, [O]riginal Crust or [C]rispy Crust: ")
    if crust.upper() == "O":
        total += original
        crustPrice = original
        c = "original"
    elif crust.upper() == 'C':
        total += crispy
        crustPrice = crispy
        c = "crispy"
elif toppings.upper() == 'C':
    crust = input(
        "\nWould you like [O]riginal Crust, [H]and Tossed crust or [S]tuffed Crust? ")
    c = ""
    crustPrice = 0
    while crust.upper() not in ['O', 'H', 'S']:
        crust = input(
            "Please enter your crust preference, [O]riginal Crust, [H]and Tossed crust or [S]tuffed Crust: ")
    if crust.upper() == "O":
        total += original
        crustPrice = original
        c = "original"
    elif crust.upper() == "H":
        total += handTossed
        crustPrice = handTossed
        c = "handTossed"
    elif crust.upper() == 'S':
        total += stuffed
        crustPrice = stuffed
        c = "stuffed"

print()
print("*" * 52)
print("Your Order Summary".center(52))
print("%-25s %-19s $%5s" %
      ("Your pizza size", "Large", "{0:.2f}".format(sizePrice)))
print("%-25s %-18s +$%5s" %
      ("Your topping option", "Veggie", "{0:.2f}".format(toppingPrice)))
print("%-25s %-18s +$%5s" %
      ("Your pizza crust", "Crispy", "{0:.2f}".format(crustPrice)))
print("="*52)
print("%-45s $%5s" % ("Total Price:", "{0:.2f}".format(total)))
