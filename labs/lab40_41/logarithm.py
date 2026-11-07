import math
from function import Function
from derivative import Derivative


class Logarithm(Function):
    def __init__(self, base):
        super().__init__("log")
        self.base = base
        print("Вызван конструктор Logarithm")

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if value <= 0 or value == 1:
            raise ValueError("Основание должно быть больше 0 и не равно 1")
        self._base = value
        self._name = "log" + str(value) + "(x)"

    def value(self, x):
        if x <= 0:
            raise ValueError("x должно быть больше 0")
        return math.log(x) / math.log(self._base)

    def derivative(self):
        return Derivative("1/(x*ln" + str(self._base) + ")", self._base)

    def info(self):
        print("Логарифм по основанию", self._base, "-", self._name)
