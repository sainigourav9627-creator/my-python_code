def decorator(func):

    def wrapper(*args):
        print("Start")
        func(*args)
        print("End")

    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(10, 20)
