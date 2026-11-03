"""Практическая работа 3: оптимизация модуля поиска простых чисел.

Задача модуля: вернуть все простые числа от 2 до limit.
Параметр оптимизации: время выполнения. Количественная характеристика, кроме времени, -
число выполненных операций деления (взятия остатка).
"""

divisions = 0  # счётчик операций % (для сравнения вариантов)


def primes_v0(limit):
    """Исходный вариант: проверяем делители от 2 до n - 1."""
    global divisions
    result = []
    for n in range(2, limit + 1):
        simple = True
        for d in range(2, n):
            divisions += 1
            if n % d == 0:
                simple = False
        if simple:
            result.append(n)
    return result


def primes_v1(limit):
    """Оптимизация 1: выход из цикла при первом делителе и предел цикла sqrt(n).

    Если у числа есть делитель, он не больше sqrt(n), а после первого найденного делителя
    дальнейшие проверки не нужны (удаление избыточных вычислений, сокращение числа итераций).
    """
    global divisions
    result = []
    for n in range(2, limit + 1):
        simple = True
        d = 2
        while d * d <= n:
            divisions += 1
            if n % d == 0:
                simple = False
                break
            d += 1
        if simple:
            result.append(n)
    return result


def primes_v2(limit):
    """Оптимизация 2: чётные числа не проверяем, делители только нечётные.

    Число 2 простое, остальные чётные числа составные. Это вдвое сокращает и перебор чисел, и перебор делителей.
    """
    global divisions
    if limit < 2:
        return []
    result = [2]
    for n in range(3, limit + 1, 2):
        simple = True
        d = 3
        while d * d <= n:
            divisions += 1
            if n % d == 0:
                simple = False
                break
            d += 2
        if simple:
            result.append(n)
    return result


def primes_v3(limit):
    """Оптимизация 3: решето Эратосфена. Деление не используется вообще, вместо него вычёркивание кратных.

    Это уже не локальное преобразование, а замена алгоритма (глобальная оптимизация).
    """
    if limit < 2:
        return []
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i::i] = bytearray(len(range(i * i, limit + 1, i)))
    return [i for i in range(2, limit + 1) if is_prime[i]]
