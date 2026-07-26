total = 0

for i in range(5,101,5):
    total = total + i

print(total)


or
  
total=0

for i in range(1,101):
    if i%5==0:
     print(i)
     total=total+i
print(total)
