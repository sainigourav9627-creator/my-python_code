num = int(input("Enter the value: "))

def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_number(num)
