def number(*args):
    for value in args:
        if value % 2 != 0:
            print(value)

number(10, 15, 20, 25, 30)
