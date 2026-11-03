"""Логарифм по произвольному основанию и натуральный логарифм."""
import math

from derivative import Derivative
from function_base import Function


class Logarithm(Function):
    """y = log_base(x). Наследник Function."""

    def __init__(self, base):
        self.base = base  # проверка основания выполняется в свойстве base
        super().__init__(f"log{self._base:g}(x)")  # вызов конструктора родителя
        self.init_chain.append("Logarithm")

    @property
    def base(self):
        """Основание логарифма: положительное число, не равное единице."""
        return self._base

    @base.setter
    def base(self, value):
        if value <= 0 or value == 1:
            raise ValueError("основание логарифма должно быть положительным и не равным 1")
        self._base = value
        self._name = f"log{value:g}(x)"  # запись функции всегда соответствует основанию

    def value(self, x):
        if x <= 0:
            raise ValueError("логарифм определён только для x > 0")
        return math.log(x) / math.log(self._base)

    def derivative(self):
        """Переопределённый виртуальный метод: точная производная 1 / (x * ln(base))."""
        return Derivative(f"1/(x*ln({self._base:g}))", lambda x: 1 / (x * math.log(self._base)), source=self)


class NaturalLogarithm(Logarithm):
    """y = ln(x). Частный случай логарифма с основанием e."""

    def __init__(self):
        super().__init__(math.e)
        self._name = "ln(x)"
        self.init_chain.append("NaturalLogarithm")

    def value(self, x):
        """Перегрузка метода родителя: ln считается напрямую, без деления на ln(base)."""
        if x <= 0:
            raise ValueError("логарифм определён только для x > 0")
        return math.log(x)

    def derivative(self):
        return Derivative("1/x", lambda x: 1 / x, source=self)
