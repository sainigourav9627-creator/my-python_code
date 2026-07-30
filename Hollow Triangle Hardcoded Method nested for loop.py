for i in range(1,6):
    for j in range(1, i+1):
        if i == 5 or j == 1 or j == i:
           print("*", end="")
        else:
           print(" ", end="")
    print()

*
**
* *
*  *
*****

Hint:                                                   

Boundary par * print hoga:

First column (j == 1)
Last column (j == i)
Last row (i == 5)
