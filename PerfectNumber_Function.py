def perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
num = int(input("Enter Number: "))
print(perfect(num))