names = ["Amit", "Ravi", "Neha"]
marks = [70, 80, 90]

result = {
    names[i]: marks[i]
    for i in range(len(names))
}

print(result)
