from itertools import zip_longest

products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000]

for index, (product, price) in enumerate(
    zip_longest(products, prices, fillvalue=0), start=101
):
    print(index, product, price)
