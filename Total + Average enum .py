from itertools import zip_longest

products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000]

total = 0

for index, (product, price) in enumerate(
    zip_longest(products, prices, fillvalue=0), start=101
):
    total = total + price
    print(index, product, price)

average = total / len(products)

print("Total:", total)
print("Average:", average)
