for i in range(1,5):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

Logic samjho

Outer loop (i) rows control karta hai.

i = 1 → Inner loop range(1,2) → *
i = 2 → Inner loop range(1,3) → **
i = 3 → Inner loop range(1,4) → ***
i = 4 → Inner loop range(1,5) → ****
i = 5 → Inner loop range(1,6) → *****

Yaani jitni row number hogi, utne hi stars print honge.
