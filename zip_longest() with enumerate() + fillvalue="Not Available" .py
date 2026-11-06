from itertools import zip_longest

products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000]

result = zip_longest(products, prices, fillvalue="Not Available")

print(dict(result))
