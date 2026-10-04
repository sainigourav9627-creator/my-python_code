from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)
