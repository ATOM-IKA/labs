from function import Function


class Derivative(Function):
    def __init__(self, name, formula):
        super().__init__(name)
        self.formula = formula
        print("Вызван конструктор Derivative")

    def value(self, x):
        return self.formula(x)
