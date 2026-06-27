age = int(input())
if age < 18:
    raise Exception("Not Eligible")
print("Eligible")