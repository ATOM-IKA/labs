import math

operators = {"def": 1, "=": 5, "[]": 1, "for": 1, "+": 1,
             "if": 1, ">": 1, "/": 1, "len()": 1, "return": 1}
operands = {"total": 4, "0": 2, "biggest": 4, "numbers": 3,
            "x": 4, "average": 2}

n1 = len(operators)
n2 = len(operands)
N1 = sum(operators.values())
N2 = sum(operands.values())
n2_star = 3

n = n1 + n2
N = N1 + N2
print("n1 =", n1, " n2 =", n2, " N1 =", N1, " N2 =", N2)
print("Словарь n =", n)
print("Длина N =", N)

N_calc = n1 * math.log2(n1) + n2 * math.log2(n2)
V = N * math.log2(n)
V_min = (2 + n2_star) * math.log2(2 + n2_star)
V_limit = (2 + n2_star * math.log2(n2_star)) * math.log2(2 + n2_star)
A = n2_star / (n2_star + 2) * math.log2(n2_star / 2)
B = n2_star - 2 * A
n2_expected = A * n1 + B
L = V_min / V
L1 = 2 * n2 / (n1 * N2)
I = L1 * V
E = V / L
T = E / 18
language = L * L * V
E0 = V_min ** 3 / language ** 2
errors = V / E0

print("Расчётная длина N' =", round(N_calc, 2))
print("Объём V =", round(V, 2))
print("Потенциальный объём V* =", round(V_min, 2))
print("Граничный объём V** =", round(V_limit, 2))
print("A =", round(A, 2), " B =", round(B, 2))
print("n2 ожидаемое =", round(n2_expected, 2))
print("Уровень программы L =", round(L, 3), " L' =", round(L1, 3))
print("Интеллектуальное содержание I =", round(I, 2))
print("Работа по программированию E =", round(E, 1))
print("Время программирования T =", round(T, 1), "с")
print("Уровень языка =", round(language, 3))
print("E0 =", round(E0, 1))
print("Число ошибок B =", round(errors, 3))
