# TODO: Prompt the user to enter Y or N for calculating a payment
cp = input("Would you like to calculate a payment(Y or N)? ")

# TODO: Add a conditional that calculates and prints a payment if the user entered Y or y
if (cp == 'y' or cp == 'Y'):
    borrowed = float(input("Enter the amount you are borrowing: "))
    loan = int(input("Enter the duration of loan in months: "))
    interest = float(input("Enter the annual interest rate: "))
    interest = (interest / 100) / 12

    m = borrowed * ((interest * (1+interest)**loan)/(((1+interest)**loan)-1))
    print(f'Your monthly payment will be {m:.2f}')

elif cp == 'n' or 'N':
    ca = input(
        "Would you like to calculate the amount you can borrow instead(Y or N)? ")

# If user choice is Y
if(ca == 'y' or ca == 'Y'):
    monthly_payment = int(input("Enter monthly payment you can afford: "))
    duration = int(input("Enter the duration of the load in months: "))
    interest = float(input("Enter tha annual interest rate: "))
    interest = (interest / 100) / 12

    # Calculating the loan amount
    payment = monthly_payment * \
        ((((1+interest)**duration)-1)/(interest * (1+interest)**duration))
    print(f"You can borrow up to {payment:.2f}")
