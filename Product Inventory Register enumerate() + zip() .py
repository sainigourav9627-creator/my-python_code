products = ["Mobile", "Laptop", "Mouse", "Keyboard"]
prices = [12000, 45000, 800, 1200]
quantity = [5, 2, 10, 8]

result = enumerate(zip(products, prices,quantity),start = 1)

print(dict(result))
