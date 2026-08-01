num=int(input("enter the number:"))
original = num
square = num * num
total = 0

while square > 0:
    digit = square % 10
    total = total + digit
    square = square // 10

if total == original:
    print("Neon Number")
else:
    print("Not Neon Number")
