numbers = {
    "a": 10,
    "b": 20,
    "c": 30
}

result = {
    key.upper(): value
    for key, value in numbers.items()
}

print(result)
