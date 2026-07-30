
A = [
    [1, 2],
    [4, 5],
    [7, 8]
]

B = [
    [1, 4],
    [4, 7],
    [7, 5]
]

for i in range(3):
    for j in range(2):
        print(A[i][j]+B[i][j],end=" ")
    print()
