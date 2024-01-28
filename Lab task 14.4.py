#Animal Class:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def eat(self):
        print("The dog is eating.")

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def eat(self):
        print("The cat is eating.")

    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def eat(self):
        print("The bird is eating seeds.")

    def make_sound(self):
        print("Tweet!")
