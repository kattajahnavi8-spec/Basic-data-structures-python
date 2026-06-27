import json
students = [
    {"name":"Ravi","marks":90},
    {"name":"Sai","marks":85}
]
with open("students.json","w") as file:
    json.dump(students,file)