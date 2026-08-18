def maximum(*args):
    maximum = args[0]

    for i in args:
        if i > maximum:
            maximum = i

    return maximum

result = maximum(10, 20, 30)
print(result)


or

def maximum(*args):
    maximum = args[0]

    for num in args:
        if num > maximum:
            maximum = num

    return maximum

result = maximum(10, 25, 7, 40, 15)

print(result)
 
