import unittest

from calculator import Calculator, arithmetic


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_operations(self):
        self.assertEqual(self.calc.arithmetic(8, 2, "+"), 10)
        self.assertEqual(self.calc.arithmetic(8, 2, "-"), 6)
        self.assertEqual(self.calc.arithmetic(8, 2, "*"), 16)
        self.assertEqual(self.calc.arithmetic(8, 2, "/"), 4)

    def test_division_is_not_integer(self):
        self.assertEqual(self.calc.arithmetic(7, 2, "/"), 3.5)

    def test_unknown_operation(self):
        self.assertEqual(self.calc.arithmetic(1, 2, "%"), "Неизвестная операция")
        self.assertEqual(self.calc.arithmetic(1, 2, ""), "Неизвестная операция")

    def test_division_by_zero(self):
        self.assertEqual(self.calc.arithmetic(5, 0, "/"), "Деление на ноль")

    def test_function(self):
        self.assertEqual(arithmetic(3, 4, "+"), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
