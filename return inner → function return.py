def outer():
    def inner():
        return 10 + 20

    return inner

result = outer()
print(result())
