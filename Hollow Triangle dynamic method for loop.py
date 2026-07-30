rows = 5

for i in range(rows):
    for j in range(i + 1):

        if j == 0 or i == rows - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


* 
* * 
*   * 
*     * 
* * * * * 
