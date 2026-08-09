def student(**data):
    total = 0

    for value in data.values():
        total = total + value

    print(total)

student(math=80, science=70, english=90)
