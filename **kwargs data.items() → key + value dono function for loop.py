def student(**data):
    for key, value in data.items():
        print(key, "=", value)

student(name="Gourav", age=25, city="Sambhal")


Output:

name = Gourav
age = 25
city = Sambhal

🧠 Rule:
.items() → key + value dono
