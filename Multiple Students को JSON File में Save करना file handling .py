import json

students = [
    {
        "name": "Gourav",
        "age": 30,
        "marks": 85
    },
    {
        "name": "Rahul",
        "age": 25,
        "marks": 90
    },
    {
        "name": "Amit",
        "age": 28,
        "marks": 78
    }
]

with open("students.json", "w") as file:
    json.dump(students, file)

print("All students saved")
