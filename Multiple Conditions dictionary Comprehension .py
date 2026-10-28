numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = {
    n: n * n
    for n in numbers
    if n > 3 and n < 8
}

print(result)
