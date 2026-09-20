class Student:

    def show_student(self):
        print("Instance Method")

    @classmethod
    def show_class(cls):
        print("Class Method")

    @staticmethod
    def show_message():
        print("Static Method")
