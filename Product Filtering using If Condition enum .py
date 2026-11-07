products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000, 500, 1500]

for index, (key, value) in enumerate(zip(products, prices), start=1):
    if value >= 10000:
        print(index, key, value)
