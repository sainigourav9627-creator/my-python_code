# -12 = 8 4 2 1                -1 = 8 4 2 1 
#     1 1 0 0  (bianry)            0 0 0 1
 
#   1s compliment                1s compliment 
#    0 0 1 1 (ulta)               1 1 1 0

#  2s compliment (add)          2s compliment
#       0 0 1 1                      1 1 1 0
#         + 1                            + 1
#  -12 =  0 1 0 0                 -1 = 1 1 1 1
   

#        0 1 0 0   (-12)  (Operator & k use)
#   &    1 1 1 1    (-1)
#   =    0 1 0 0

# 1s compliment = 1 0 1 1 
# 2s compliment =     + 1
#             = 1 1 0 0    (-12 & -1) bitwise operator   
                           
#  8 4 2 1
#  1 1 0 0 =  -12answer  


a=-12&-1
b=-8&-5         
c=-5&-6
d=-9&-4
print(a)
print(b)
print(c)
print(d)
