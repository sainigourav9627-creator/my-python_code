matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

max = 0

for row in matrix:
    for value in row:
        if value > max:
            max = value

print(max)
