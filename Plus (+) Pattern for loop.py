rows = 5

middle = rows // 2

for i in range(rows):
    for j in range(rows):

        if i == middle or j == middle:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

    *     
    *     
* * * * * 
    *     
    *     
