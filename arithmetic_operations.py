num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Addition of ", num1, " and ", num2, " is: ", num1 + num2)
print("Subtraction of ", num1, " and ", num2, " is: ", num1 - num2) 
print("Multiplication of ", num1, " and ", num2, " is: ", num1 * num2)
if num2 != 0:
    print("Division of ", num1, " and ", num2, " is: ", num1 / num2)    
else:    print("Division: Cannot divide by zero")
print("Modulus of ", num1, " and ", num2, " is: ", num1 % num2)