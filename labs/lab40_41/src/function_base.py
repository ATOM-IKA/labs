"""Базовый класс функции одной переменной."""


class Function:
    """Функция одной переменной y = f(x).

    Поля:
        _name       - строковая запись функции, например "log2(x)"
        init_chain  - список имён классов, конструкторы которых были вызваны
                      (нужен, чтобы показать вызов конструктора родителя)
    """

    def __init__(self, name):
        self._name = name
        self.init_chain = ["Function"]

    @property
    def name(self):
        """Запись функции (только чтение)."""
        return self._name

    def value(self, x):
        """Значение функции в точке x. Виртуальный метод: определяется в наследниках."""
        raise NotImplementedError("метод value() должен быть определён в наследнике")

    def derivative(self):
        """Возвращает объект, представляющий производную текущего экземпляра.

        Виртуальный метод. Реализация по умолчанию считает производную численно
        (центральная разность), поэтому подходит для любой функции. Наследники,
        знающие формулу производной, переопределяют метод и возвращают точный результат.
        """
        from derivative import Derivative
        step = 1e-6
        return Derivative(f"({self.name})'", lambda x: (self.value(x + step) - self.value(x - step)) / (2 * step),
                          source=self)

    def describe(self):
        return f"{type(self).__name__}: y = {self.name}"
