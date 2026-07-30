A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [1, 6, 3],
    [4, 7, 6],
    [8, 0, 9]
]

for i in range(3):
    for j in range(3):
        total = 0

        for k in range(3):
            total = total + A[i][k] * B[k][j]

        print(total, end=" ")

    print()
