from itertools import zip_longest

products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000]

result = zip_longest(products, prices, fillvalue=0)


print(dict(result))
