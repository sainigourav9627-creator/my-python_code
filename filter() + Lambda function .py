filter() = condition के हिसाब से items चुनना  

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda n: n % 2 == 0, numbers))

print(result)
