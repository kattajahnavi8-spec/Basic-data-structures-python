def total(marks):
    return sum(marks)
def percentage(marks):
    return sum(marks) / len(marks)
def grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    else:
        return "D"
marks = [85, 90, 78, 88, 92]
tot = total(marks)
per = percentage(marks)
print("Total:", tot)
print("Percentage:", per)
print("Grade:", grade(per))