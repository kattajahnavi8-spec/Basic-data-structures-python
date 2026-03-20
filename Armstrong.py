n=int(input("Enter a number: "))
temp=n
s=0
while n:
    d=n%10
    s+=d**3
    n//=10
if temp==s:
    print(temp,"is an armstrong number")        
else:
    print(temp,"is not an armstrong number")    