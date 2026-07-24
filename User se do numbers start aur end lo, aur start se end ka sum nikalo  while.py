start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

i = start
total = 0

while i <= end:
    total = total + i
    i = i + 1
print("Sum =", total)
