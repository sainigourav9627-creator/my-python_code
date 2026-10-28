numbers = [1, 2, 3, 4, 5]

result = {
    n: "Even" if n % 2 == 0 else "Odd"
    for n in numbers
}

print(result)
