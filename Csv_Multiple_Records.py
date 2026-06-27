import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    n = int(input("How many students? "))
    for i in range(n):
        roll = input("Roll: ")
        name = input("Name: ")
        marks = input("Marks: ")
        writer.writerow([roll, name, marks])