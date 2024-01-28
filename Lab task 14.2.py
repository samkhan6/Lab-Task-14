#Vehicle Interface:
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starting")

    def stop(self):
        print("Car stopping")

    def move(self):
        print("Car moving")

class Bike(Vehicle):
    def start(self):
        print("Bike starting")

    def stop(self):
        print("Bike stopping")

    def move(self):
        print("Bike moving")

class Plane(Vehicle):
    def start(self):
        print("Plane starting")

    def stop(self):
        print("Plane stopping")

    def move(self):
        print("Plane flying")
