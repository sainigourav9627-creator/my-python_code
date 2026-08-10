def decorator(func):

    def wrapper(name):
        print("Start")
        func(name)
        print("End")

    return wrapper


@decorator
def hello(name):
    print("Hello", name)


hello("Gourav")
