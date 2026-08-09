def test(**data):
    print(data)

test(a=10, b=20)


def student(**data):
    print(data)

student(name="Gourav", age=25, city="Sambhal")



Output:
{'name': 'Gourav', 'age': 25, 'city': 'Sambhal'}

Yahan data poori dictionary hai.

🧠 Rule:
**kwargs → key=value ko dictionary mein collect karta hai.

