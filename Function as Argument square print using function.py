इसका मतलब है एक function को दूसरे function के parameter के रूप में देना।

def square(n):
    return n * n

def calculate(func, num):
    return func(num)

print(calculate(square, 5))
