def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


def hello():
    print("Hello")


hello = decorator(hello)

hello()

Decorator ऐसा function है जो किसी दूसरे function में extra behavior जोड़ता है, बिना original function का code बदले।

याद रखने की Trick

Decorator = पुराने function के ऊपर extra काम लगाना 🎯
