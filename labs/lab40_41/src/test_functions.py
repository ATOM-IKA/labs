import math
import unittest

from function_base import Function
from logarithm import Logarithm, NaturalLogarithm


class FunctionTests(unittest.TestCase):
    def test_values(self):
        self.assertAlmostEqual(Logarithm(2).value(8), 3.0)
        self.assertAlmostEqual(Logarithm(10).value(1000), 3.0)
        self.assertAlmostEqual(NaturalLogarithm().value(math.e), 1.0)

    def test_domain(self):
        for bad in (0, -2):
            with self.assertRaises(ValueError):
                Logarithm(2).value(bad)
            with self.assertRaises(ValueError):
                NaturalLogarithm().value(bad)

    def test_base_property(self):
        for bad in (1, 0, -3):
            with self.assertRaises(ValueError):
                Logarithm(bad)

    def test_name_follows_base(self):
        log = Logarithm(2)
        self.assertEqual(log.name, "log2(x)")
        log.base = 10
        self.assertEqual(log.name, "log10(x)")

    def test_exact_derivative(self):
        self.assertAlmostEqual(Logarithm(2).derivative().value(4), 1 / (4 * math.log(2)))
        self.assertAlmostEqual(NaturalLogarithm().derivative().value(5), 0.2)

    def test_numeric_derivative_of_base_class(self):
        class Square(Function):
            def __init__(self):
                super().__init__("x^2")

            def value(self, x):
                return x * x

        self.assertAlmostEqual(Square().derivative().value(3), 6.0, places=4)

    def test_second_derivative_uses_inherited_method(self):
        second = NaturalLogarithm().derivative().derivative()
        self.assertAlmostEqual(second.value(2), -0.25, places=4)

    def test_constructor_chain(self):
        self.assertEqual(NaturalLogarithm().init_chain, ["Function", "Logarithm", "NaturalLogarithm"])

    def test_abstract_value(self):
        with self.assertRaises(NotImplementedError):
            Function("f").value(1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
