def student(**data):
    print(data.values())

student(name="Gourav", age=25, city="Sambhal")  

Output roughly:
dict_values(['Gourav', 25, 'Sambhal'])

Agar values ko ek-ek karke print karna ho:

def student(**data):
    for value in data.values():
        print(value)

student(name="Gourav", age=25, city="Sambhal")

Output:
Gourav
25
Sambhal

🧠 Rule:
.values() → sirf values




