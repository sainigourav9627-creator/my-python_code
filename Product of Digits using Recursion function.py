def product_digits(n):
    if n == 0:
        return 1

    digit = n % 10
    return digit * product_digits(n // 10)

print(product_digits(1234))
