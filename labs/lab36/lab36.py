class Calculator:
    def arithmetic(self, a, b, operation):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Неизвестная операция"


calc = Calculator()
print(calc.arithmetic(8, 2, "+"))
print(calc.arithmetic(8, 2, "-"))
print(calc.arithmetic(8, 2, "*"))
print(calc.arithmetic(8, 2, "/"))
print(calc.arithmetic(7, 2, "/"))
print(calc.arithmetic(8, 2, "%"))
