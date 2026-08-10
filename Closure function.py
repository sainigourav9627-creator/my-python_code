Closure क्या होता है?

जब inner function, outer function के variable को याद रखता है, even जब outer function का execution खत्म हो चुका हो।


def outer():
    x = 10

    def inner():
        print(x)

    return inner

result = outer()
result()


Closure = Inner function का outer function के variable को याद रखना।
