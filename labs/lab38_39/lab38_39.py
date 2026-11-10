class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

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


print(TriangleChecker([3, 4, 5]).is_triangle())
print(TriangleChecker([2, 2, 2]).is_triangle())
print(TriangleChecker([1, 2, 3]).is_triangle())
print(TriangleChecker([10, 1, 1]).is_triangle())
print(TriangleChecker([-3, 4, 5]).is_triangle())
print(TriangleChecker(["3", 4, 5]).is_triangle())
print(TriangleChecker([3.5, 4.5, 6.0]).is_triangle())
