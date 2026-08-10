def numbers():
    yield 10
    return
    yield 20

for x in numbers():
    print(x)

    
