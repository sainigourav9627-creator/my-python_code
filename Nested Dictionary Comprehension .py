students = ["Amit", "Ravi"]
subjects = ["Math", "English"]

result = {
    name: {subject: 0 for subject in subjects}
    for name in students
}

print(result)
