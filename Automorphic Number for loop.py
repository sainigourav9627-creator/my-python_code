
Definition
Automorphic Number woh hota hai jiska square usi number par end hota hai.

num = int(input("Enter the number:"))

square = num * num
digits = len(str(num))

if square % (10 ** digits) == num:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")



1
5
6
25
76
376
625
9376
