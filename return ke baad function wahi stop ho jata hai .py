def test():
    return 10
    print("Hello")

test()

or

Lekin ek important baat: output screen par kuch nahi dikhega, kyunki return 10 value wapas bhej deta hai, aur aapne us returned value ko print() nahi kiya.
print("Hello") bhi execute nahi hoga, kyunki return ke baad function wahi stop ho jata hai.

def test():
    return 10
    print("Hello")
result=test()
print(result)
