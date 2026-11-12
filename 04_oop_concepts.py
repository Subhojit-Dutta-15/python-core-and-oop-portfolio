"""
================================================================================
04. Object-Oriented Programming (OOP) in Python
================================================================================
Overview:
    Complete demonstration of the four pillars of Object-Oriented Programming—
    Encapsulation, Abstraction, Inheritance, and Polymorphism—along with decorators
    and magic (dunder) methods.

Key Concepts Covered:
    - Classes & Constructors: __init__, instance vs. class attributes
    - Encapsulation: Private attributes (__balance, __acc_pass) and controlled access
    - Inheritance & super(): Single, multi-level, and multiple inheritance
    - Decorators: @staticmethod, @classmethod, and @property
    - Polymorphism: Operator overloading via dunder methods (__add__, __gt__)
"""

import math


# ------------------------------------------------------------------------------
# 1. Encapsulation & Bank Account Simulation
# ------------------------------------------------------------------------------
class BankAccount:
    def __init__(self, acc_no, balance, pin):
        self.acc_no = acc_no
        self.__balance = balance  # Private attribute
        self.__pin = pin          # Private attribute

    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"[{self.acc_no}] Credited: {amount}. New Balance: {self.__balance}")

    def debit(self, amount, pin):
        if pin != self.__pin:
            print("Invalid PIN. Transaction denied.")
            return
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"[{self.acc_no}] Debited: {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    @property
    def balance(self):
        return self.__balance


# ------------------------------------------------------------------------------
# 2. Inheritance, super() & @property Decorator
# ------------------------------------------------------------------------------
class Employee:
    company = "TechCorp"

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    def show_details(self):
        print(f"Company: {self.company} | Role: {self.role} | Dept: {self.dept} | Salary: {self.salary}")


class Engineer(Employee):
    def __init__(self, name, age, salary="1,00,000 INR"):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", salary)

    def show_details(self):
        print(f"Name: {self.name} | Age: {self.age}")
        super().show_details()


# ------------------------------------------------------------------------------
# 3. Polymorphism & Dunder Methods (__add__, __gt__)
# ------------------------------------------------------------------------------
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __str__(self):
        return f"{self.real}i + {self.img}j"


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __gt__(self, other):
        return self.radius > other.radius


if __name__ == "__main__":
    acc = BankAccount(2005, 50000, 2468)
    acc.credit(5000)
    acc.debit(10000, 2468)

    eng = Engineer("Subhojit Dutta", 21)
    eng.show_details()

    c1, c2 = ComplexNumber(2, 3), ComplexNumber(4, 5)
    print("Complex Sum:", c1 + c2)

    circle1, circle2 = Circle(10), Circle(7)
    print(f"Circle 1 Area: {circle1.area:.2f} | Circle 1 > Circle 2: {circle1 > circle2}")
