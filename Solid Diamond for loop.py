rows = 5

# Upper Half
for i in range(rows):

    # Spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Stars
    for j in range(2 * i + 1):
        print("*", end="")

    print()

# Lower Half
for i in range(rows - 2, -1, -1):

    # Spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Stars
    for j in range(2 * i + 1):
        print("*", end="")

    print()


    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
