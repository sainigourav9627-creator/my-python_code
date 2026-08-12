def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


tower_of_hanoi(3, "A", "B", "C")

Base Case
if n == 1:
    print("Move disk 1 from", source, "to", destination)
    return

tower_of_hanoi(n - 1, auxiliary, source, destination)


Interview में याद रखने वाला logic
Tower of Hanoi:

1. n-1 → Source to Auxiliary
2. 1   → Source to Destination
3. n-1 → Auxiliary to Destination

और:

Minimum moves = 2ⁿ - 1

⭐⭐⭐ Tower of Hanoi recursion का classic example है क्योंकि इसमें एक function के अंदर खुद के दो recursive calls होते हैं।
