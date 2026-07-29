matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#row print

print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])

#matrix[row][column]

print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])

#matrix[row]

print(matrix[1][0])

print(matrix[1][1])
print(matrix[1][2])

#row[column]

print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])

for row in matrix:
    for value in row:
        print(value,end=" ")
    print()

