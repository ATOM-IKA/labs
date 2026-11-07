class Calculator:
    def arithmetic(self, a, b, operation):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b == 0:
                return "Деление на ноль"
            return a / b
        else:
            return "Неизвестная операция"


class Second:
    color = "red"
    form = "circle"

    def changecolor(self, newcolor):
        self.color = newcolor

    def changeform(self, newform):
        self.form = newform


class YesInit:
    def __init__(self, one, two):
        self.fname = one
        self.sname = two


class NoInit:
    def names(self, one, two):
        self.fname = one
        self.sname = two


def arithmetic(a, b, operation):
    return Calculator().arithmetic(a, b, operation)


obj1 = Second()
obj2 = Second()
print(obj1.color, obj1.form)
print(obj2.color, obj2.form)
obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changeform("oval")
print(obj1.color, obj1.form)
print(obj2.color, obj2.form)

first = YesInit("Peter", "Ok")
print(first.fname, first.sname)
second = NoInit()
second.names("Peter", "Ok")
print(second.fname, second.sname)

calc = Calculator()
print(calc.arithmetic(8, 2, "+"))
print(calc.arithmetic(8, 2, "-"))
print(calc.arithmetic(8, 2, "*"))
print(calc.arithmetic(8, 2, "/"))
print(calc.arithmetic(7, 2, "/"))
print(calc.arithmetic(8, 2, "%"))
print(calc.arithmetic(5, 0, "/"))
print(arithmetic(1.5, 2, "*"))
