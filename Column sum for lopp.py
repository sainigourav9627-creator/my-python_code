
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(3):      # column
    total = 0

    for j in range(3):  # row
        total = total + matrix[j][i]

    print(total)
