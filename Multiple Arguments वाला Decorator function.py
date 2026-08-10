def decorator(func):

    def wrapper(a, b):
        print("Start")
        func(a, b)
        print("End")

    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(10, 20)
