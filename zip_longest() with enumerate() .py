from itertools import zip_longest

names = ["Aman", "Rahul", "Amit"]
marks = [80, 90]

result = enumerate(zip_longest(names, marks), start=1)

print(list(result))
