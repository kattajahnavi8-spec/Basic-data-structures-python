def armstrong(n):
    digits = len(str(n))
    total = sum(int(d)**digits for d in str(n))
    return total == n
num = int(input("Enter Number: "))
if armstrong(num):
    print("Armstrong Number")
else:
    print("Not Armstrong")