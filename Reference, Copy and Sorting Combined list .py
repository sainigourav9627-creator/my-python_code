a = [10, 20, 30]
b = a
c = a.copy()

b.append(40)
c.append(50)

print("a =", a)
print("b =", b)
print("c =", c)

print("Sorted =", sorted(c))

c.sort(reverse=True)
print("Descending =", c)
