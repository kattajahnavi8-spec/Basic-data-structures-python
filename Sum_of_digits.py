n=int(input("Enter a number: "))
sum=0
while n:
    sum+=n%10
    n//=10      
print("Sum of digits of given number ", n, " is:", sum)    