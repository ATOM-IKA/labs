"""Лабораторная работа 38-39: класс TriangleChecker и перегрузка методов."""

MESSAGE_OK = "Ура, можно построить треугольник!"
MESSAGE_NEGATIVE = "С отрицательными числами ничего не выйдет!"
MESSAGE_NOT_NUMBER = "Нужно вводить только числа!"
MESSAGE_FAIL = "Жаль, но из этого треугольник не сделать."


def is_number(value):
    """Число в смысле задания: int или float, но не bool и не строка."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


class TriangleChecker:
    """Проверяет, можно ли составить треугольник из трёх отрезков."""

    def __init__(self, first, second, third):
        self.sides = [first, second, third]

    def is_triangle(self):
        if not all(is_number(side) for side in self.sides):
            return MESSAGE_NOT_NUMBER
        if any(side < 0 for side in self.sides):
            return MESSAGE_NEGATIVE
        a, b, c = sorted(self.sides)
        # длина каждой стороны должна быть меньше суммы двух других,
        # для отсортированных сторон достаточно проверить самую большую
        if a > 0 and a + b > c:
            return MESSAGE_OK
        return MESSAGE_FAIL

    # перегрузка операторов (теоретическая часть работы)
    def __getitem__(self, index):
        """checker[0] возвращает сторону по индексу."""
        return self.sides[index]

    def __call__(self, first, second, third):
        """checker(3, 4, 5) задаёт новые стороны и сразу возвращает результат проверки."""
        self.sides = [first, second, third]
        return self.is_triangle()

    def __str__(self):
        return "TriangleChecker" + str(tuple(self.sides))
