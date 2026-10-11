a = [[10, 11], [30, 40], [23, 60]]

minimum = a[0][0]
maximum = a[0][0]

for row in a:
    for num in row:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

print("Minimum =", minimum)
print("Maximum =", maximum)
