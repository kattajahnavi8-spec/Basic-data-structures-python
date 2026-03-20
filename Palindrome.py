n=int(input("enter number: "))
temp=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if temp==rev:
    print("Given number",temp," is a palindrome") 
else:    
    print("Given number",temp," is not a palindrome")       