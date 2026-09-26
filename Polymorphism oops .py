Poly = Many
Morph = Forms

यानी एक ही method/interface का अलग-अलग objects के लिए अलग behavior।


class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()
