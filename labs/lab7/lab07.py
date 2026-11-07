def check_side(x):
    return 0.1 <= x <= 100


print("Эквивалентное разбиение")
classes = [("меньше допустимого", 0.05), ("допустимые значения", 5), ("больше допустимого", 150)]
for name, value in classes:
    print(f"  {name:20} x = {value:<6} принимается: {check_side(value)}")

print("Граничные значения")
for value in (0.09, 0.1, 0.11, 99.99, 100, 100.01):
    print(f"  x = {value:<7} принимается: {check_side(value)}")

print("Таблица решений для длины и ширины")
print("  длина  ширина  результат")
for length in (True, False):
    for width in (True, False):
        if length and width:
            result = "площадь вычислена"
        elif not length:
            result = "ошибка в длине"
        else:
            result = "ошибка в ширине"
        print(f"  {str(length):6} {str(width):7} {result}")

print("Предположение об ошибке")
for text in ("4,5", " 5 ", "nan", "inf", "1e3", "0,0001"):
    try:
        value = float(text.replace(",", "."))
        print(f"  {text!r:9} -> {value} принимается: {check_side(value)}")
    except ValueError:
        print(f"  {text!r:9} -> не число")
