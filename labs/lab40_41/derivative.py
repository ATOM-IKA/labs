import math
from function import Function


class Derivative(Function):
    def __init__(self, name, base):
        super().__init__(name)
        self.base = base
        print("Вызван конструктор Derivative")

    def value(self, x):
        return 1 / (x * math.log(self.base))
