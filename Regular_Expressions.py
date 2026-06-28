import re
text = "Ravi scored 95 marks in 2025"
numbers = re.findall(r'\d+', text)
print(numbers)