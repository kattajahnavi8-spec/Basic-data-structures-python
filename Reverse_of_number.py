n=int(input("Enter number to reverse: "))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse of the number", n, "is: ", rev)