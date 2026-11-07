import math
from logarithm import Logarithm
from derivative import Derivative


class NaturalLogarithm(Logarithm):
    def __init__(self):
        super().__init__(math.e)
        self._name = "ln(x)"
        print("Вызван конструктор NaturalLogarithm")

    def value(self, x):
        if x <= 0:
            raise ValueError("x должно быть больше 0")
        return math.log(x)

    def derivative(self):
        return Derivative("1/x", math.e)
