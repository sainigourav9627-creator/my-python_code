a = [[10, 11], [30, 41], [23, 60]]
total = 0

for row in a:
    for num in row:
        if num % 2 == 0:
            total = total + num

print("Even Sum =", total)
