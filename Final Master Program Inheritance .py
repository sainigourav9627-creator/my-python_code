class Person:

    school = "ABC School"          # Class Variable

    def __init__(self, name, age):
        self.name = name           # Instance Variable
        self._age = age            # Protected Variable
        self.__id = 101            # Private Variable

    def show(self):                # Instance Method
        print("Name:", self.name)
        print("Age:", self._age)

    def get_id(self):              # Getter
        return self.__id

    @classmethod
    def school_name(cls):          # Class Method
        print("School:", cls.school)

    @staticmethod
    def welcome():                 # Static Method
        print("Welcome")


class Student(Person):             # Inheritance

    def __init__(self, name, age, course):
        super().__init__(name, age) # Parent Constructor
        self.course = course

    def show(self):                # Method Overriding
        super().show()             # Parent Method
        print("Course:", self.course)


s = Student("Gourav", 25, "BCA")

s.show()

print("ID:", s.get_id())

Student.school_name()
Student.welcome()

print(isinstance(s, Student))
print(isinstance(s, Person))
print(issubclass(Student, Person))
