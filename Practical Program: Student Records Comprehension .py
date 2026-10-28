students = {
    101: {"name": "Amit", "age": 20, "marks": 75},
    102: {"name": "Ravi", "age": 21, "marks": 85},
    103: {"name": "Neha", "age": 19, "marks": 90}
}

for student_id, data in students.items():
    print("ID:", student_id)
    print("Name:", data["name"])
    print("Marks:", data["marks"])
    print("----------")
