
for i in range(1,5):
    for j in range(1,i+1):
        print( ?, end=" ")
    print()


Sirf print(?) badlega. Output bhi usi ke hisaab se badlega.

print() me kya hai?	Output
print("*")	text\n*\n* *\n* * *\n* * * *\n
print(i)	text\n1\n2 2\n3 3 3\n4 4 4 4\n
print(j)	text\n1\n1 2\n1 2 3\n1 2 3 4\n
print(i, j)	text\n1 1\n2 1 2 2\n3 1 3 2 3 3\n4 1 4 2 4 3 4 4\n
print(i*j)	text\n1\n2 4\n3 6 9\n4 8 12 16\n
print(num)	text\n1\n2 3\n4 5 6\n7 8 9 10\n

1️⃣ print("*")
Har baar star print karo.

2️⃣ print(i)
Row number print karo.

3️⃣ print(j)
Column number print karo.

4️⃣ print(i, j)
Row aur Column dono print karo.

5️⃣ print(i*j)
Row × Column print karo.

6️⃣ print(num)
Ek alag variable lagatar badhta rahega.



Golden Formula
Outer Loop (i) = Rows

Inner Loop (j) = Columns / Har row me kitni baar print hoga

print(...) = Screen par kya dikhega

Matlab:

i ➜ Row
j ➜ Column
print(...) ➜ Final output
