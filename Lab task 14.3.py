#Calculator Interfaces:
from abc import ABC, abstractmethod

class Operator(ABC):
    @abstractmethod
    def operate(self, x, y):
        pass

class Adder(Operator):
    def operate(self, x, y):
        return x + y

class Subtractor(Operator):
    def operate(self, x, y):
        return x - y

class Multiplier(Operator):
    def operate(self, x, y):
        return x * y

class Divider(Operator):
    def operate(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
