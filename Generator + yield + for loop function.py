🧠 Ek line mein

अंदर वाला for → values बनाता है।
बाहर वाला for → values लेता और print करता है।

Aur yield ki wajah se function har value dene ke baad pause hota hai, poora function ek saath close nahi hota.

def numbers():
    for i in range(1, 6):
        yield i

for x in numbers():
    print(x)
