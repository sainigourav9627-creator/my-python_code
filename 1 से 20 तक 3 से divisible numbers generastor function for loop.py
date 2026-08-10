def divisible():
    for i in range(1, 21):
        if i % 3 == 0:
            yield i

for x in divisible():
    print(x)
