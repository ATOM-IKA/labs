"""Расписание занятий, построенное на базе множества (наследование)."""
from sets import MySet

DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]


class Lesson:
    """Одна пара: день недели, номер пары, название курса."""

    def __init__(self, day, number, course):
        if day not in DAYS:
            raise ValueError(f"неизвестный день недели: {day}")
        if not 1 <= number <= 7:
            raise ValueError("номер пары должен быть от 1 до 7")
        self.day = day
        self.number = number
        self.course = course

    def __eq__(self, other):
        return isinstance(other, Lesson) and (self.day, self.number, self.course) == (other.day, other.number, other.course)

    def __hash__(self):
        return hash((self.day, self.number, self.course))

    def __str__(self):
        return f"{self.number}. {self.course}"


class Schedule(MySet):
    """Множество пар. В одной ячейке «день + номер пары» может стоять только одна пара."""

    def add(self, lesson):
        """Переопределённый метод множества: занятая ячейка расписания отклоняется."""
        if self.find(lesson.day, lesson.number) is not None:
            raise ValueError(f"{lesson.day}, пара {lesson.number} уже занята")
        super().add(lesson)

    def _new_empty(self):
        return Schedule()

    def find(self, day, number):
        for lesson in self:
            if lesson.day == day and lesson.number == number:
                return lesson
        return None

    def day_lessons(self, day):
        """Пары одного дня, по возрастанию номера."""
        return sorted((lesson for lesson in self if lesson.day == day), key=lambda lesson: lesson.number)

    def show_day(self, day):
        lessons = self.day_lessons(day)
        if not lessons:
            return f"{day}: занятий нет"
        return "\n".join([f"{day}:"] + [f"  {lesson}" for lesson in lessons])

    def show_week(self):
        return "\n".join(self.show_day(day) for day in DAYS if self.day_lessons(day))

    def edit_course(self, day, number, new_course):
        """Меняет название курса у существующей пары."""
        lesson = self.find(day, number)
        if lesson is None:
            raise KeyError(f"{day}, пара {number}: такой пары нет")
        self.remove(lesson)
        super().add(Lesson(day, number, new_course))
