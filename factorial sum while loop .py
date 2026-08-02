n=int(input("enter the value:"))

fact=1
total=0
i=1

while i<=n:
    fact=fact*i
    total=total+i
    i=i+1

print(fact)
print(total)
