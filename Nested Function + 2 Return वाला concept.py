def employee():

    salary = "30000"

    def details():

        def show():
            return salary

        return show()

    final = details()
    print(final)

employee()
