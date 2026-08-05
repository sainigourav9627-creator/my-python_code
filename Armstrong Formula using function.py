num = int(input("Enter the value: "))

def armstrong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        num = num // 10
        total = total + digit ** 3

    if total == original:
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong(num)
