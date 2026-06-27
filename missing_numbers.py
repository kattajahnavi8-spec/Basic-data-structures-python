numbers = [1, 2, 4, 6, 7, 9]
missing = []
for i in range(numbers[0], numbers[-1] + 1):
    if i not in numbers:
        missing.append(i)
print("Missing Numbers:", missing)