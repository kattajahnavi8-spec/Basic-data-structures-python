def calculate_amount(quantity, price):
    return quantity * price
def calculate_discount(amount):
    if amount >= 5000:
        return amount * 0.10      # 10% discount
    elif amount >= 2000:
        return amount * 0.05      # 5% discount
    else:
        return 0
def calculate_tax(amount):
    return amount * 0.18          # 18% GST
product = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))
amount = calculate_amount(quantity, price)
discount = calculate_discount(amount)
subtotal = amount - discount
tax = calculate_tax(subtotal)
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