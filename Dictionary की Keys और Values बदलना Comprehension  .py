marks = {
    "Amit": 30,
    "Ravi": 40,
    "Neha": 50
}

result = {
    name: score * 2
    for name, score in marks.items()
}

print(result)
