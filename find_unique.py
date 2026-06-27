numbers = [1,2,2,3,4,4,5,6]
unique = []
for num in numbers:
    if numbers.count(num)==1:
        unique.append(num)
print("Unique Elements: ",unique)         