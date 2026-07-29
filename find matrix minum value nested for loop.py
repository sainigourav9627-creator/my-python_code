matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

min = 9

for row in matrix:
    for value in row:
        if value < min:
            min = value

print(min)
