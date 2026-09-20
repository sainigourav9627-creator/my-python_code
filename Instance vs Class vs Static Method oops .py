class Student:

    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")


s1 = Student()

s1.instance_method()
Student.class_method()
Student.static_method()
