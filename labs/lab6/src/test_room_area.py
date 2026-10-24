import subprocess
import sys
import unittest

from room_area import InputError, room_area, total_area, parse_side


class RoomAreaTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(room_area(4, 5), 20.0)
        self.assertEqual(room_area("4,5", "3"), 13.5)
        self.assertEqual(total_area([(4, 3), (2, 2)]), 16.0)

    def test_boundaries(self):
        self.assertEqual(room_area(0.1, 0.1), 0.01)
        self.assertEqual(room_area(100, 100), 10000.0)
        for bad in (0.09, 100.01):
            with self.assertRaises(InputError):
                parse_side(bad)

    def test_negative(self):
        for bad in ("", "  ", "abc", "0", "-3", "nan", "inf", "1e3", None):
            with self.assertRaises(InputError, msg=repr(bad)):
                parse_side(bad)
        with self.assertRaises(InputError):
            total_area([])

    def test_cli(self):
        out = subprocess.run([sys.executable, "room_area.py"], input="4\n5\n\n",
                             capture_output=True, text=True).stdout
        self.assertIn("20.00", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
