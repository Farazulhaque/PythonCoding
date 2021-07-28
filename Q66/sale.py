loop = True
saleID = []
saleAmt = []
discountPercent = []
discountAmount = []
while loop == True:
    x = int(input("Enter sale ID: "))
    if x != -1:
        y = int(input("Enter sale amount: "))
        z = float(input("Enter discount percent: "))
        saleID.append(x)
        saleAmt.append(y)
        discountPercent.append(z)
        discountAmount.append(y - (y * z/100))
    else:
        loop = False
print("saleId \t Sale Amount \t Discount Percent \t Discount Amount")
for i in range(len(saleID)):
    print(
        f"{saleID[i]} \t\t {saleAmt[i]} \t {discountPercent[i]} \t\t\t {discountAmount[i]}")

print(f"Number of sales that were processed {len(saleID)}")
print(
    f"the total amount of discounts given (in dollars) {sum(discountAmount)}$")
print(
    f"average discount amount (in dollars) {sum(discountAmount)/len(discountAmount)}$")

