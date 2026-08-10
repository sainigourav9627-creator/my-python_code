def decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


@decorator            test = decorator(test)   yeh use huya h baki same h ko diffrent nhi h prohram m
def test():
    print("Hello")


test()


Function को decorator से wrap करना
