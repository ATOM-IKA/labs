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
        text = ""
        for item in self.items:
            text = text + str(item) + ", "
        return "{" + text[:-2] + "}"


class Lesson:
    def __init__(self, day, number, course):
        self.day = day
        self.number = number
        self.course = course

    def __eq__(self, other):
        if self.day != other.day or self.number != other.number:
            return False
        return self.course == other.course

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
        print(day + ":")
        found = False
        for number in range(1, 8):
            for lesson in self.items:
                if lesson.day == day and lesson.number == number:
                    print("  " + str(lesson))
                    found = True
        if not found:
            print("  занятий нет")

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
schedule.add_lesson("Понедельник", 1, "Математика")
schedule.add_lesson("Понедельник", 2, "Информатика")
schedule.add_lesson("Понедельник", 3, "Английский язык")
schedule.add_lesson("Вторник", 1, "Программирование")
schedule.add_lesson("Вторник", 2, "Физическая культура")
schedule.add_lesson("Среда", 2, "Математика")
schedule.add_lesson("Среда", 3, "Основы алгоритмизации")
schedule.add_lesson("Четверг", 1, "Информатика")
schedule.add_lesson("Четверг", 2, "Английский язык")
schedule.add_lesson("Четверг", 3, "Русский язык")
schedule.add_lesson("Пятница", 1, "Программирование")
schedule.add_lesson("Пятница", 2, "История")

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
