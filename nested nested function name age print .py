def person():

    name = "Gourav"
    age = 20

    def info():

        def display():
            print("Name:", name)
            print("Age:", age)

        display()

    info()

person()
