class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]

    def is_triangle(self):
        for side in self.sides:
            if type(side) not in (int, float):
                return "Нужно вводить только числа!"
        for side in self.sides:
            if side < 0:
                return "С отрицательными числами ничего не выйдет!"
        a, b, c = sorted(self.sides)
        if a > 0 and a + b > c:
            return "Ура, можно построить треугольник!"
        return "Жаль, но из этого треугольник не сделать."

    def __getitem__(self, index):
        return self.sides[index]

    def __call__(self, a, b, c):
        self.sides = [a, b, c]
        return self.is_triangle()

    def __str__(self):
        return "Стороны: " + str(self.sides)


tests = [(3, 4, 5), (1, 2, 3), (2, 2, 2), (10, 1, 1), (-3, 4, 5), (0, 4, 4), ("3", 4, 5), (3, None, 5), (3.5, 4.5, 6.0)]
for sides in tests:
    checker = TriangleChecker(*sides)
    print(checker, "->", checker.is_triangle())

checker = TriangleChecker(3, 4, 5)
print(checker[0], checker[2])
print(checker(6, 8, 15))
print(checker)
