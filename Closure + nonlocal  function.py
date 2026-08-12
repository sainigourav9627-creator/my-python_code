def counter():
    count = 0

    def increase():
        nonlocal count
        count = count + 1
        return count

    return increase

c = counter()

print(c())
print(c())
print(c())
