rows = 5

for i in range(rows):

    # Spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Stars
    for j in range(2 * i + 1):
        print("*", end="")

    print()
