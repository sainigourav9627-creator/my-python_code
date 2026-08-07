def minimum(*args):
    minimum = args[0]

    for i in args:
        if i < minimum:
            minimum = i

    return minimum

result = minimum(10, 2, 30)
print(result)
 
