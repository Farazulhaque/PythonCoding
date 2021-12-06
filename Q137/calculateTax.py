# State Key
stateKey = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")


# your code starts here
def getInfo():
    productInfo = []
    moreItem = True
    while moreItem == True:
        quantity = int(
            input('Please enter amount of quantity (enter 0 if finish): '))
        if quantity == 0:
            moreItem = False
        else:
            itemWeight = float(input('Please enter the weight of Item: '))
            itemCost = float(input('Please enter cost of Item: '))
            print()
            productInfo.append([quantity, itemWeight, itemCost])
    return productInfo


# Calculation
def calculate(productInfoList):
    boxWeight = 0
    subTotal = 0
    for i in range(len(productInfoList)):
        quantity, itemWeight, itemCost = productInfoList[i]
        boxWeight = boxWeight + (quantity * itemWeight)
        subTotal = subTotal + (quantity * itemCost)
        shipping = boxWeight * .25
        if boxWeight < 10:
            handling = 1
        elif boxWeight > 100:
            handling = 5
        else:
            handling = 3
        shippingAndHandling = shipping + handling
    return (subTotal, shippingAndHandling)


# main
# Welcome Statement
while True:
    print('This program should let the user enter any number of items into the program')
    print('and then calculate and output the Subtotal, Tax (if CA), Shipping and Handling, and Total Due')
    print()

    state = input(
        'Please Enter the two letter abbriviation of State the package is being ship: ')
    state = state.upper()
    print()

    productInfoList = getInfo()

    subTotal, shippingAndHandling = calculate(productInfoList)

    if state in stateKey:
        tax = subTotal * .08
    else:
        tax = 0.00
    totalDue = subTotal + shippingAndHandling + tax

    print()
    print(format('Subtotal:', '<25'), format(subTotal, '>10,.2f'))
    print(format('Tax:', '<25'), format(tax, '>10,.2f'))
    print(format('Shipping and Handling:', '<25'),
          format(shippingAndHandling, '>10,.2f'))
    print(format('Total Due: ', '<25'), format(totalDue, '>10,.2f'))
    # code ends here
    choice = input("Do you want to enter the data again?[Y/n]: ")
    if choice.lower() != 'y':
        break
