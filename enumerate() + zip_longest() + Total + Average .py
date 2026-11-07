from itertools import zip_longest

products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000]

result = enumerate(
    zip_longest(products, prices, fillvalue=0),
    start=101
)

total = 0
count = 0

for index, (product, price) in result:
    print(index, product, price)
    total += price
    count += 1

print("Total:", total)
print("Average:", total / count)
