numbers = [1,2,3,4,4,5,6,7,8,2,8]
duplicates =[]
for num in numbers:
    if numbers.count(num)>1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate elements: ",duplicates)        