import unittest

from triangle import (MESSAGE_FAIL, MESSAGE_NEGATIVE, MESSAGE_NOT_NUMBER, MESSAGE_OK, TriangleChecker)


class TriangleCheckerTests(unittest.TestCase):
    def check(self, *sides):
        return TriangleChecker(*sides).is_triangle()

    def test_valid(self):
        self.assertEqual(self.check(3, 4, 5), MESSAGE_OK)
        self.assertEqual(self.check(2, 2, 2), MESSAGE_OK)
        self.assertEqual(self.check(3.5, 4.5, 6.0), MESSAGE_OK)

    def test_degenerate(self):
        self.assertEqual(self.check(1, 2, 3), MESSAGE_FAIL)
        self.assertEqual(self.check(10, 1, 1), MESSAGE_FAIL)
        self.assertEqual(self.check(0, 4, 4), MESSAGE_FAIL)

    def test_negative(self):
        self.assertEqual(self.check(-3, 4, 5), MESSAGE_NEGATIVE)
        self.assertEqual(self.check(3, 4, -5), MESSAGE_NEGATIVE)

    def test_not_numbers(self):
        self.assertEqual(self.check("3", 4, 5), MESSAGE_NOT_NUMBER)
        self.assertEqual(self.check(3, None, 5), MESSAGE_NOT_NUMBER)
        self.assertEqual(self.check(True, 2, 2), MESSAGE_NOT_NUMBER)

    def test_order_of_sides_does_not_matter(self):
        self.assertEqual(self.check(5, 3, 4), MESSAGE_OK)
        self.assertEqual(self.check(3, 5, 4), MESSAGE_OK)


if __name__ == "__main__":
    unittest.main(verbosity=2)
