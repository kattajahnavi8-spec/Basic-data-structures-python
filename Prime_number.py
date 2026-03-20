n=int(input("enter number: "))
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
        break
if flag:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")