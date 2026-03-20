n=int(input("enter number: "))
a=0
b=1
print("fibonacci series: ")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print("\nThere are ",n,"numbers in the fibonacci series")
