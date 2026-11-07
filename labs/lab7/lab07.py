def check_side(x):
    return 0.1 <= x <= 100


print("Эквивалентное разбиение")
print("меньше допустимого, x = 0.05:", check_side(0.05))
print("допустимое значение, x = 5:", check_side(5))
print("больше допустимого, x = 150:", check_side(150))

print("Граничные значения")
for x in [0.09, 0.1, 0.11, 99.99, 100, 100.01]:
    print("x =", x, check_side(x))

print("Таблица решений")
for length_ok in [True, False]:
    for width_ok in [True, False]:
        if length_ok and width_ok:
            result = "площадь вычислена"
        elif not length_ok:
            result = "ошибка в длине"
        else:
            result = "ошибка в ширине"
        print("длина:", length_ok, "ширина:", width_ok, "->", result)

print("Предположение об ошибке")
for text in ["4,5", " 5 ", "nan", "inf", "1e3", "0,0001"]:
    x = float(text.replace(",", "."))
    print(repr(text), x, check_side(x))
