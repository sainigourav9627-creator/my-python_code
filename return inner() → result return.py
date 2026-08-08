def outer():
    def inner():
        return 10 + 40

    return inner()

result = outer()
print(result)
