a = [30, 10, 20]

a.append(40)
a.insert(1, 15)
a.remove(30)

print("Current List =", a)
print("Length =", len(a))
print("Minimum =", min(a))
print("Maximum =", max(a))

a.sort()
print("Ascending =", a)

a.reverse()
print("Reversed =", a)
