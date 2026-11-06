students = ["Aman", "Rahul", "Amit"]
maths = [80, 70, 90]
science = [75, 85, 95]

result = enumerate(zip(students, maths,science),start = 1)

print(dict(result))
