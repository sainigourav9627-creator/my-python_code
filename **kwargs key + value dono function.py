def employee(**data):
    for key,value in data.items():
       print(key, "=", value)
employee(name="Amit",sallary=25000,city="delhi")
