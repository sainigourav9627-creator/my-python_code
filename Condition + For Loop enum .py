products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000, 500, 1500]

for index, (product, price) in enumerate(zip(products, prices), start=1):
    if price >= 10000:
        print(index, product, price)
