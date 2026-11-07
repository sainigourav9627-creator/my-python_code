products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000, 500, 1500]

total = 0

for index, (key, value) in enumerate(zip(products, prices), start=1):
    total = total + value
    print(index, key, value)

average = total / len(products)

print("Total:", total)
print("Average:", average)
print("Product Names:", list(products))
