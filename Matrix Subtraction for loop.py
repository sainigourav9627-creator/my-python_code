A = [
    [6, 8],
    [8, 9]
]

B = [
    [1, 6],
    [2, 5]
]

for i in range(2):
    for j in range(2):
        print(A[i][j] - B[i][j], end=" ")
    print()
