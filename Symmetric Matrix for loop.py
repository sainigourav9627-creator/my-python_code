Symmetric Matrix = Transpose aur Original Matrix bilkul same hote hain.

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

flag = True

for i in range(3):
    for j in range(3):
        if matrix[i][j] != matrix[j][i]:
            flag = False

if flag:
    print("Symmetric Matrix")
else:
    print("Not Symmetric Matrix")
