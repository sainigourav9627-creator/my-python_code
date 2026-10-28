numbers = [1, 2, 3, 4, 5]

result = {n: n * 2 for n in numbers if n > 3}

print(result)




numbers = [1, 2, 3, 4, 5]

result = {
    n: "Big" if n > 3 else "Small"
    for n in numbers
}

print(result)





