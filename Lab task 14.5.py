#Employee Class:
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_pay(self):
        pass

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

class FullTimeEmployee(Employee):
    def calculate_pay(self):
        return self.salary / 12  # Monthly pay for full-time employees

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked
