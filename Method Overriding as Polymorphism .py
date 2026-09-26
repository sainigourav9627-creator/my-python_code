class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):                 # NEW: Method Overriding
        print("Bark")


class Cat(Animal):
    def sound(self):                 # NEW: Method Overriding
        print("Meow")


def make_sound(animal):
    animal.sound()


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)
