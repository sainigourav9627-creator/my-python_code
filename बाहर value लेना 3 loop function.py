def student():
    marks = 80

    def result():

        def show():
            return marks

        return show()

    final = result()
    print(final)

student()
