Generator Function kya hai?

Aisa function jo values ko ek-ek karke deta hai, ek saath saari values nahi.
Generator banane ke liye yield use hota hai.

def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)


yield kya karta hai?
yield function ko value deta hai aur wahi par temporarily pause kar deta hai.

    def numbers():
    yield 1
    yield 2
    yield 3
