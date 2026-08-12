def armstrong(n, total=0):
    if n == 0:
        return total

    digit = n % 10
    total = total + digit ** 3

    return armstrong(n // 10, total)
