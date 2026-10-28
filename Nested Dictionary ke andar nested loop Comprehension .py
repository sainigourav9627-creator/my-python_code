students = {
    "Amit": {"age": 20, "marks": 75},
    "Ravi": {"age": 21, "marks": 85}
}

for name, data in students.items():
    print(name)

    for key, value in data.items():
        print(key, value)
