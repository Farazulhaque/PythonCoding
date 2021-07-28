def applyDiscount(saleAmount, discountPercent):
    discountAmount = saleAmount - (saleAmount * discountPercent/100)
    return discountAmount


print(f"Discount amount is: {applyDiscount(100.00, 10.00)}")
