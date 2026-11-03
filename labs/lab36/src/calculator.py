"""Лабораторная работа 36, вариант 1: простейшие арифметические операции."""


class Calculator:
    """Выполняет арифметическую операцию над двумя числами."""

    def arithmetic(self, first, second, operation):
        """Возвращает результат операции + - * / над first и second.

        Для любой другой операции возвращает строку «Неизвестная операция».
        """
        if operation == "+":
            return first + second
        if operation == "-":
            return first - second
        if operation == "*":
            return first * second
        if operation == "/":
            if second == 0:
                return "Деление на ноль"
            return first / second
        return "Неизвестная операция"


def arithmetic(first, second, operation):
    """Функция из условия задания: делегирует вычисление объекту Calculator."""
    return Calculator().arithmetic(first, second, operation)
