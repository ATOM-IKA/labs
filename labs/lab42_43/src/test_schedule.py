import unittest

from schedule import Lesson, Schedule
from sets import MySet


class MySetTests(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(len(MySet([1, 1, 2, 2, 2])), 2)

    def test_contains(self):
        s = MySet([1, 2])
        self.assertTrue(s.contains(1))
        self.assertFalse(s.contains(5))

    def test_union_and_intersection(self):
        a, b = MySet([1, 2, 3]), MySet([3, 4])
        self.assertEqual(sorted(a.union(b)), [1, 2, 3, 4])
        self.assertEqual(sorted(a.intersection(b)), [3])
        self.assertEqual(len(a.intersection(MySet())), 0)

    def test_operations_do_not_change_operands(self):
        a, b = MySet([1, 2]), MySet([2, 3])
        a.union(b)
        a.intersection(b)
        self.assertEqual(sorted(a), [1, 2])
        self.assertEqual(sorted(b), [2, 3])


class ScheduleTests(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule([])
        self.schedule.add(Lesson("Вторник", 2, "Физика"))
        self.schedule.add(Lesson("Вторник", 1, "Математика"))
        self.schedule.add(Lesson("Среда", 1, "Информатика"))

    def test_day_is_sorted_by_number(self):
        self.assertEqual([lesson.number for lesson in self.schedule.day_lessons("Вторник")], [1, 2])

    def test_empty_day(self):
        self.assertEqual(self.schedule.show_day("Пятница"), "Пятница: занятий нет")

    def test_week_lists_days_in_order(self):
        text = self.schedule.show_week()
        self.assertLess(text.index("Вторник"), text.index("Среда"))

    def test_edit_course(self):
        self.schedule.edit_course("Вторник", 1, "Алгебра")
        self.assertEqual(self.schedule.find("Вторник", 1).course, "Алгебра")
        self.assertEqual(len(self.schedule), 3)

    def test_edit_missing_lesson(self):
        with self.assertRaises(KeyError):
            self.schedule.edit_course("Пятница", 1, "Алгебра")

    def test_occupied_cell_is_rejected(self):
        with self.assertRaises(ValueError):
            self.schedule.add(Lesson("Вторник", 1, "Другое"))

    def test_invalid_lesson(self):
        with self.assertRaises(ValueError):
            Lesson("Воскресенье", 1, "X")
        with self.assertRaises(ValueError):
            Lesson("Вторник", 9, "X")

    def test_union_returns_schedule(self):
        other = Schedule([Lesson("Четверг", 1, "Химия")])
        merged = self.schedule.union(other)
        self.assertIsInstance(merged, Schedule)
        self.assertEqual(len(merged), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
