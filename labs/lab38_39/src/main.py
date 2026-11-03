from triangle import TriangleChecker

cases = [(3, 4, 5), (1, 2, 3), (2, 2, 2), (10, 1, 1), (-3, 4, 5), (3, 4, -5), (0, 4, 4), ("3", 4, 5), (3, None, 5), (3.5, 4.5, 6.0), (True, 2, 2)]
for sides in cases:
    checker = TriangleChecker(*sides)
    print(f"{str(checker):32} -> {checker.is_triangle()}")

print("--- перегруженные методы ---")
checker = TriangleChecker(3, 4, 5)
print("checker[0] =", checker[0], "; checker[2] =", checker[2])
print("checker(6, 8, 15) ->", checker(6, 8, 15))
print("print(checker):", checker)
