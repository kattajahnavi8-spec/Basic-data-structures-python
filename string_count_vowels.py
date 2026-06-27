s = input("Enter a string: ")
print("The string is: ", s)
count = 0
for ch in s.lower():
    if ch in 'aeiou':
        count += 1
print("The number of vowels in the string is: ", count)