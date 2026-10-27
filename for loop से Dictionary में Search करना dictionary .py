students = {
    "Gourav": 85,
    "Amit": 70,
    "Rahul": 90
}

search_name = "Amit"

for name, marks in students.items():
    if name == search_name:
        print(name, marks)
