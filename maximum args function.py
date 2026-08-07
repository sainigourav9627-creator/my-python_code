def maximum(*args):
    maximum = args[0]

    for i in args:
        if i > maximum:
            maximum = i

    return maximum

result = maximum(10, 20, 30)
print(result)
 
