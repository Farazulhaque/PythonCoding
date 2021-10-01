originalbill = float(input("How much is your original bill? "))
percentageTip = float(input("What percentage is your tip? "))

tipAmount = originalbill * percentageTip/100
totalBill = originalbill + tipAmount

print()
print("-"*35)
print(f"Your tip based on {percentageTip:.2f}% is {tipAmount:.2f}.")
print(f"Your total bill is {totalBill:.2f}.")
print("-"*35)

