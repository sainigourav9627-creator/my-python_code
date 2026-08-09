def student(**data):

    # 1. Puri dictionary
    print("1. Dictionary:")
    print(data)

    # 2. Ek particular key ki value
    print("\n2. Name ki value:")
    print(data["name"])

    # 3. Sirf values
    print("\n3. Sirf values:")
    for value in data.values():
        print(value)

    # 4. Key + value dono
    print("\n4. Key + Value:")
    for key, value in data.items():
        print(key, "=", value)


student(name="Gourav", age=25, city="Sambhal")


Output:
1. Dictionary:
{'name': 'Gourav', 'age': 25, 'city': 'Sambhal'}

2. Name ki value:
Gourav

3. Sirf values:
Gourav
25
Sambhal

4. Key + Value:
name = Gourav
age = 25
city = Sambhal



🧠 Ab 4 rules ekdum pakke:
data
↓
पूरी Dictionary

data["name"]
↓
एक particular value

for value in data.values()
↓
सिर्फ values

for key, value in data.items()
↓
key + value दोनों

सबसे important difference:
for value in data.values() → 1 variable (value)
for key, value in data.items() → 2 variables (key, value)
