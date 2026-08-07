def prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        return "prime"
    else:
        return "not prime"

result = prime(7)
print(result)
