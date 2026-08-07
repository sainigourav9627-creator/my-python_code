def factorail(num):
   fact=1
   for i in range(1,num+1):
    fact=fact*i
   return fact
result=factorail(5)
print(result)
