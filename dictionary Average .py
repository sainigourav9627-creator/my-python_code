students = {
    101: {"name": "Amit", "marks": 80},
    102: {"name": "Neha", "marks": 90},
    103: {"name": "Rahul", "marks": 65}
}

total = 0
count = 0

for student_id, details in students.items():
    total = total + details["marks"]
    count = count + 1

average = total / count

print("Average", average)
