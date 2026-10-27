students = {
    "S1": {"name": "Gourav", "marks": 85},
    "S2": {"name": "Amit", "marks": 90}
}

for student_id, details in students.items():
    print(student_id, details["name"], details["marks"])
