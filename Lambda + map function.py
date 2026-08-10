numbers = [1, 2, 3, 4]

result = list(map(lambda n: n * 2, numbers))

print(result)


सबसे जरूरी

map(lambda n: n * 2, numbers)

lambda n: n * 2 → क्या operation करना है
numbers → किस list पर करना है
map() → हर element पर operation लगाएगा
list() → result को list में बदलता है
