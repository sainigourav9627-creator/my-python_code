numbers = (10, 20, 30, 40, 50)

search = 35

for num in numbers:
    if num == search:
        print("Found")
        break
else:
    print("Not Found")
