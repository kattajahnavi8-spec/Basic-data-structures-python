a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if(a>b and a>c):
    print("a=",a,"is the greatest number")
elif(b>a and b>c):
    print("b=",b,"is the greatest number")
else:
    print("c=",c,"is the greatest number")