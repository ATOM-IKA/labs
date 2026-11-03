"""Демонстрация к лабораторной работе 36: классы, объекты, конструктор и методы."""
from calculator import Calculator, arithmetic


class Second:
    """Пример из теории: атрибуты класса и методы, меняющие их у отдельного объекта."""
    color = "red"
    form = "circle"

    def changecolor(self, newcolor):
        self.color = newcolor

    def changeform(self, newform):
        self.form = newform


class YesInit:
    """Класс с конструктором: атрибуты создаются при создании объекта."""

    def __init__(self, one, two):
        self.fname = one
        self.sname = two


class NoInit:
    """Класс без конструктора: атрибуты появляются только после вызова метода."""

    def names(self, one, two):
        self.fname = one
        self.sname = two


print("--- Класс Second (атрибуты класса, два объекта) ---")
obj1 = Second()
obj2 = Second()
print(obj1.color, obj1.form)
print(obj2.color, obj2.form)
obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changeform("oval")
print(obj1.color, obj1.form)
print(obj2.color, obj2.form)

print("--- Конструктор: YesInit и NoInit ---")
first = YesInit("Peter", "Ok")
print(first.fname, first.sname)
second = NoInit()
second.names("Peter", "Ok")
print(second.fname, second.sname)

print("--- Вариант 1: класс Calculator ---")
calc = Calculator()
for a, b, op in [(8, 2, "+"), (8, 2, "-"), (8, 2, "*"), (8, 2, "/"), (7, 2, "/"), (8, 2, "%"), (5, 0, "/")]:
    print(f"arithmetic({a}, {b}, {op!r}) = {calc.arithmetic(a, b, op)!r}")
print("Функция arithmetic(1.5, 2, '*') =", arithmetic(1.5, 2, "*"))
