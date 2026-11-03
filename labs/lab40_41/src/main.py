"""Демонстрация работы всех классов (лабораторная работа 40-41, вариант 13)."""
import math

from derivative import Derivative
from function_base import Function
from logarithm import Logarithm, NaturalLogarithm


def show(function, points):
    print(function.describe())
    for x in points:
        print(f"    f({x}) = {function.value(x):.6f}")


print("=== Конструкторы: цепочка вызовов ===")
log2 = Logarithm(2)
ln = NaturalLogarithm()
print("Logarithm(2):      ", " -> ".join(log2.init_chain))
print("NaturalLogarithm():", " -> ".join(ln.init_chain))

print("\n=== Свойства ===")
print("log2.name =", log2.name, "; log2.base =", log2.base)
log2.base = 10
print("после log2.base = 10:  base =", log2.base, "; name =", log2.name)
try:
    log2.base = 1
except ValueError as error:
    print("log2.base = 1 ->", error)
log2 = Logarithm(2)

print("\n=== Метод value() ===")
show(log2, [1, 2, 8, 0.5])
show(ln, [1, math.e, 10])
try:
    ln.value(-1)
except ValueError as error:
    print("ln.value(-1) ->", error)

print("\n=== Перегруженный value() у NaturalLogarithm и Logarithm(e) ===")
same = Logarithm(math.e)
print(f"ln(5) через NaturalLogarithm = {ln.value(5):.10f}")
print(f"ln(5) через Logarithm(e)     = {same.value(5):.10f}")

print("\n=== Виртуальный метод derivative() ===")
d_log2 = log2.derivative()
d_ln = ln.derivative()
print(d_log2.describe(), "| цепочка:", " -> ".join(d_log2.init_chain))
print(d_ln.describe())
for x in (1, 2, 4):
    exact = d_log2.value(x)
    print(f"    (log2)'({x}) = {exact:.6f}   проверка 1/({x}*ln2) = {1 / (x * math.log(2)):.6f}")
for x in (1, 2, 4):
    print(f"    (ln)'({x})   = {d_ln.value(x):.6f}   проверка 1/{x} = {1 / x:.6f}")

print("\n=== derivative() у Derivative (метод не переопределён, берётся из Function) ===")
second = d_ln.derivative()
print(second.describe())
for x in (1, 2, 4):
    print(f"    (ln)''({x}) = {second.value(x):.6f}   точное значение -1/{x}^2 = {-1 / x ** 2:.6f}")

print("\n=== Базовый класс Function ===")
print(Function("f(x)").describe())
try:
    Function("f(x)").value(1)
except NotImplementedError as error:
    print("Function.value ->", error)

print("\n=== Принадлежность к классам ===")
print("isinstance(ln, Logarithm):", isinstance(ln, Logarithm), "; isinstance(ln, Function):", isinstance(ln, Function))
print("isinstance(d_ln, Derivative):", isinstance(d_ln, Derivative), "; isinstance(d_ln, Logarithm):", isinstance(d_ln, Logarithm))
