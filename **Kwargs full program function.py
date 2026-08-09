def student(**data):

    # 1. Puri dictionary
    print(data)

    # 2. Ek particular key ki value
    print(data["name"])

    # 3. Sirf values
    print(data.values())

    # 4. Key + value dono
    print(data.items())


student(name="Gourav", age=25, city="Sambhal")


Output roughly:
{'name': 'Gourav', 'age': 25, 'city': 'Sambhal'}

Gourav

dict_values(['Gourav', 25, 'Sambhal'])

dict_items([('name', 'Gourav'), ('age', 25), ('city', 'Sambhal')])


Ab difference dekho
data
↓
पूरी dictionary
{'name': 'Gourav', 'age': 25, 'city': 'Sambhal'}

data["name"]
↓
एक value
Gourav

data.values()
↓
सिर्फ values
Gourav, 25, Sambhal

data.items()
↓
key + value
name Gourav
age 25
city Sambhal

