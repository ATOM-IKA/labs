from logarithm import Logarithm
from natural_logarithm import NaturalLogarithm

print("Создание объектов")
log2 = Logarithm(2)
print()
ln = NaturalLogarithm()
print()

print("Метод info()")
log2.info()
ln.info()
print()

print("Значения функций")
for x in (1, 2, 8):
    print("log2(" + str(x) + ") =", log2.value(x))
for x in (1, 10):
    print("ln(" + str(x) + ") =", round(ln.value(x), 4))
print()

print("Производные")
d1 = log2.derivative()
d2 = ln.derivative()
d1.info()
d2.info()
for x in (1, 2, 4):
    print("(log2)'(" + str(x) + ") =", round(d1.value(x), 4), " (ln)'(" + str(x) + ") =", round(d2.value(x), 4))
print()

print("Свойство base")
log2.base = 10
print(log2.name, log2.base)
try:
    log2.base = 1
except ValueError as error:
    print("Ошибка:", error)
try:
    ln.value(-1)
except ValueError as error:
    print("Ошибка:", error)
