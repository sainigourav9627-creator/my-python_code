numbers = (45, 20, 85, 10, 60)

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)
