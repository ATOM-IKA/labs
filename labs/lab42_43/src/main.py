"""Меню для работы с расписанием (лабораторная работа 42-43).

Запуск без аргументов открывает меню. Команды читаются с ввода, поэтому программу
можно проверить и скриптом: python3 main.py < commands.txt
"""
from schedule import DAYS, Lesson, Schedule


def default_schedule():
    schedule = Schedule()
    for day, number, course in [
        ("Понедельник", 1, "Математика"), ("Понедельник", 2, "Информатика"), ("Понедельник", 3, "Английский язык"),
        ("Вторник", 1, "Программирование"), ("Вторник", 2, "Физическая культура"),
        ("Среда", 2, "Математика"), ("Среда", 3, "Основы алгоритмизации"),
        ("Четверг", 1, "Информатика"), ("Четверг", 2, "Английский язык"), ("Четверг", 3, "Русский язык"),
        ("Пятница", 1, "Программирование"), ("Пятница", 2, "История"),
    ]:
        schedule.add(Lesson(day, number, course))
    return schedule


MENU = "1 - всё расписание, 2 - один день, 3 - изменить название курса, 0 - выход"


def main():
    schedule = default_schedule()
    while True:
        print(MENU)
        command = input("Команда: ").strip()
        if command == "1":
            print(schedule.show_week())
        elif command == "2":
            day = input("День недели: ").strip()
            print(schedule.show_day(day) if day in DAYS else "Неизвестный день недели")
        elif command == "3":
            day = input("День недели: ").strip()
            try:
                number = int(input("Номер пары: "))
            except ValueError:
                print("Ошибка: номер пары должен быть целым числом")
                continue
            try:
                schedule.edit_course(day, number, input("Новое название курса: ").strip())
                print("Готово")
            except (ValueError, KeyError) as error:
                print("Ошибка:", error.args[0])
        elif command == "0":
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
