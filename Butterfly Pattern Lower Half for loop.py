rows = 5

# Lower Half
for i in range(rows - 1, 0, -1):

    # Left Stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for j in range(2 * (rows - i)):
        print(" ", end="")

    # Right Stars
    for j in range(i):
        print("*", end="")

    print()
