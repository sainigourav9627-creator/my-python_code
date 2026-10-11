a = [[10, 11], [30, 40], [23, 60]]
found = False

for row in a:
    for num in row:
        if num == 23:
            found = True

if found:
    print("Found")
else:
    print("Not Found")
