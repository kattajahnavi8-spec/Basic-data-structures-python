product = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))
amount = quantity * price
if amount >= 5000:
    discount = amount * 0.10
elif amount >= 2000:
    discount = amount * 0.05
else:
    discount = 0
subtotal = amount - discount
tax = subtotal * 0.18
final_bill = subtotal + tax
print("\n----- BILL RECEIPT -----")
print("Product Name :", product)
print("Quantity     :", quantity)
print("Unit Price   :", price)
print("Amount       :", amount)
print("Discount     :", discount)
print("Subtotal     :", subtotal)
print("GST (18%)    :", tax)
print("Final Bill   :", final_bill)