from sets import MySet

a = MySet([1, 2, 3, 3, 4])
b = MySet([3, 4, 5])
print("A =", a, " |A| =", len(a))
print("B =", b)
print("3 принадлежит A:", a.contains(3), "; 7 принадлежит A:", a.contains(7), "; 5 in B:", 5 in b)
print("A объединить B  =", a.union(b))
print("A пересечь B    =", a.intersection(b))
print("A пересечь пустое =", a.intersection(MySet()))
words = MySet(["кот", "пёс"]).union(MySet(["пёс", "ёж"]))
print("Строки:", words)
