employee = ["Gourav", "Aman", "Rahul"]
salary = [15000, 18000, 20000]

result = enumerate(zip(employee, salary),start = 1)

print(tuple(result))
