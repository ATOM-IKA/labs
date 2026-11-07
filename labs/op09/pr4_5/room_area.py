def read_side(text):
    text = text.replace(",", ".")
    try:
        side = float(text)
    except ValueError:
        print("Ошибка: нужно ввести число")
        return None
    if not 0.1 <= side <= 100:
        print("Ошибка: размер должен быть от 0.1 до 100 м")
        return None
    return side


def room_area(length, width):
    a = read_side(length)
    b = read_side(width)
    if a is None or b is None:
        return None
    return round(a * b, 2)


def main():
    total = 0
    number = 1
    while True:
        length = input(f"Участок {number}, длина (м): ")
        if length == "" and number > 1:
            break
        width = input(f"Участок {number}, ширина (м): ")
        area = room_area(length, width)
        if area is None:
            continue
        total += area
        number += 1
    print(f"Площадь помещения: {total:.2f} м2")


if __name__ == "__main__":
    main()
