"""Класс для представления производных."""
from function_base import Function


class Derivative(Function):
    """Производная некоторой функции, заданная вычисляющей её функцией.

    Метод derivative() здесь не переопределяется: берётся реализация из Function,
    то есть вторая производная вычисляется численно.
    """

    def __init__(self, name, evaluate, source=None):
        super().__init__(name)  # вызов конструктора родителя
        self._evaluate = evaluate
        self.source = source
        self.init_chain.append("Derivative")

    def value(self, x):
        return self._evaluate(x)
