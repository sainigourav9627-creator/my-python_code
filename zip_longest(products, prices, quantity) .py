from itertools import zip_longest

products = ["Mobile", "Laptop", "Mouse"]
prices = [12000, 45000]
quantity = [2, 1, 5]

result = zip_longest(products, prices, quantity, fillvalue=0)

print(list(result))
