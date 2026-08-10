def numbers():
    yield 10
    yield 20
    yield 30

g = numbers()

print(next(g))
print(next(g))
print(next(g))


Difference

yield	                 next()
Function के अंदर	          Function के बाहर
Value produce करता है	 Value लेता है
Pause करता है	         Generator को आगे चलाता है

Important: next() generator के साथ ही काम करता है। yield generator बनाने का मुख्य हिस्सा है।
