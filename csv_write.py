import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll", "Name", "Marks"])
    writer.writerow([101, "Ravi", 90])