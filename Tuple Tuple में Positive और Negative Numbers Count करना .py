numbers = (10, -5, 20, -15, 30, -2)

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print(positive)
print(negative)
