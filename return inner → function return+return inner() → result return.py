सबसे important difference
Code	Kya return hota hai?

return inner	   Function
return inner()	    Function ka result

Aapne dono ko compare karke exactly sahi concept pakda hai. ✅

Ab next hum Nested Function + parameter + returned inner function karenge.

def outer():
    def inner():
        return 10+50

    return inner

result = outer()
print(result())


def outer():
    def inner():
        return 10+40

    return inner()

result = outer()
print(result)
