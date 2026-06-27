m1 = float(input("Enter marks in Maths: "))
m2 = float(input("Enter marks in Data structures: "))
m3 = float(input("Enter marks in English: "))
avg = (m1+m2+m3)/3
if avg >= 90:
    print("Grade A")
elif avg >= 75:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
else:
    print("Grade D")