class MySet:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def contains(self, item):
        return item in self.items

    def union(self, other):
        result = MySet()
        for item in self.items:
            result.add(item)
        for item in other.items:
            result.add(item)
        return result

    def intersection(self, other):
        result = MySet()
        for item in self.items:
            if other.contains(item):
                result.add(item)
        return result

    def __str__(self):
        return "{" + ", ".join(str(item) for item in self.items) + "}"


class Lesson:
    def __init__(self, day, number, course):
        self.day = day
        self.number = number
        self.course = course

    def __eq__(self, other):
        return self.day == other.day and self.number == other.number and self.course == other.course

    def __str__(self):
        return str(self.number) + ". " + self.course


class Schedule(MySet):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    def add_lesson(self, day, number, course):
        for lesson in self.items:
            if lesson.day == day and lesson.number == number:
                print("Эта пара уже занята")
                return
        self.add(Lesson(day, number, course))

    def show_day(self, day):
        lessons = [lesson for lesson in self.items if lesson.day == day]
        lessons.sort(key=lambda lesson: lesson.number)
        print(day + ":")
        if not lessons:
            print("  занятий нет")
        for lesson in lessons:
            print("  " + str(lesson))

    def show_week(self):
        for day in self.days:
            self.show_day(day)

    def change_course(self, day, number, new_course):
        for lesson in self.items:
            if lesson.day == day and lesson.number == number:
                lesson.course = new_course
                return True
        return False


a = MySet()
for x in [1, 2, 3, 3, 4]:
    a.add(x)
b = MySet()
for x in [3, 4, 5]:
    b.add(x)
print("A =", a)
print("B =", b)
print("3 принадлежит A:", a.contains(3))
print("7 принадлежит A:", a.contains(7))
print("Объединение:", a.union(b))
print("Пересечение:", a.intersection(b))
print()

schedule = Schedule()
data = [
    ("Понедельник", 1, "Математика"), ("Понедельник", 2, "Информатика"), ("Понедельник", 3, "Английский язык"),
    ("Вторник", 1, "Программирование"), ("Вторник", 2, "Физическая культура"),
    ("Среда", 2, "Математика"), ("Среда", 3, "Основы алгоритмизации"),
    ("Четверг", 1, "Информатика"), ("Четверг", 2, "Английский язык"), ("Четверг", 3, "Русский язык"),
    ("Пятница", 1, "Программирование"), ("Пятница", 2, "История"),
]
for day, number, course in data:
    schedule.add_lesson(day, number, course)

while True:
    print()
    print("1 - расписание на неделю")
    print("2 - расписание на день")
    print("3 - изменить название курса")
    print("0 - выход")
    command = input("Команда: ")
    if command == "1":
        schedule.show_week()
    elif command == "2":
        day = input("День недели: ")
        schedule.show_day(day)
    elif command == "3":
        day = input("День недели: ")
        number = int(input("Номер пары: "))
        course = input("Новое название: ")
        if schedule.change_course(day, number, course):
            print("Название изменено")
        else:
            print("Такой пары нет")
    elif command == "0":
        break
