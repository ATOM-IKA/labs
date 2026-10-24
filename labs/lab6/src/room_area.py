"""Программа вычисления площади помещения (лабораторная работа 6, вариант 13).

Помещение задаётся одним или несколькими прямоугольными участками (Г-образная
комната = два участка). Размеры вводятся в метрах, допустима запятая.
"""
import math
import sys

__version__ = "1.0"

MIN_SIDE = 0.1
MAX_SIDE = 100.0


class InputError(ValueError):
    """Некорректные входные данные."""


def parse_side(value, name="сторона"):
    if value is None or str(value).strip() == "":
        raise InputError(f"{name}: значение не введено")
    try:
        number = float(str(value).strip().replace(",", "."))
    except ValueError:
        raise InputError(f"{name}: введите число, получено «{value}»")
    if not math.isfinite(number):
        raise InputError(f"{name}: значение должно быть конечным числом")
    if number <= 0:
        raise InputError(f"{name}: значение должно быть больше нуля")
    if number < MIN_SIDE or number > MAX_SIDE:
        raise InputError(f"{name}: допустимый диапазон {MIN_SIDE}–{MAX_SIDE} м")
    return number


def room_area(length, width):
    """Площадь прямоугольной комнаты, м², округление до 0,01."""
    return round(parse_side(length, "длина") * parse_side(width, "ширина"), 2)


def total_area(parts):
    """Площадь составной комнаты: сумма прямоугольных участков (length, width)."""
    if not parts:
        raise InputError("не задано ни одного участка")
    return round(sum(room_area(l, w) for l, w in parts), 2)


def main(argv=None):
    print("Расчёт площади помещения. Размеры в метрах. Пустая длина завершает ввод участков.")
    parts = []
    try:
        while True:
            length = input(f"Участок {len(parts) + 1}, длина: ")
            if length.strip() == "" and parts:
                break
            width = input(f"Участок {len(parts) + 1}, ширина: ")
            room_area(length, width)
            parts.append((length, width))
        print(f"Площадь помещения: {total_area(parts):.2f} м²")
        return 0
    except InputError as err:
        print(f"Ошибка: {err}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
