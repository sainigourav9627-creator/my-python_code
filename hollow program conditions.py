Yaad rakhne ka Rule
Pattern	Condition

Hollow Square	i==0 or i==rows-1 or j==0 or j==cols-1
Hollow Triangle	j==0 or i==j or i==rows-1
Hollow Pyramid	j==0 or j==2*i or i==rows-1
X Pattern	i==j or i+j==rows-1
Plus (+)	i==middle or j==middle

Important: X Pattern ke liye rows aur cols same hone chahiye, yani square (5×5, 7×7, 9×9...). Rectangle (4×8) mein X symmetric nahi dikhega.
