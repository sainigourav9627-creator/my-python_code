class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


def make_sound(animal):
    animal.sound()


d = Dog()
c = Cat()
c = Cow()

make_sound(d)
make_sound(c)
make_sound(c)
