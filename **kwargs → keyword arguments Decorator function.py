def decorator(func):

    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wrapper


@decorator
def greet(name, age):
    print(name, age)


greet("Amit", 20)


याद रखो

*args → positional arguments
**kwargs → keyword arguments
Decorator में दोनों साथ → किसी भी तरह के arguments handle कर सकते हैं ✅
