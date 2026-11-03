"""Абстрактная структура данных «множество»."""


class MySet:
    """Множество без повторяющихся элементов.

    Элементы хранятся в списке, поэтому от них требуется только сравнение на равенство
    (хешируемость не нужна, в множество можно класть и объекты-записи).
    """

    def __init__(self, items=()):
        self._items = []
        for item in items:
            self.add(item)

    def add(self, item):
        """Добавляет элемент, если его ещё нет."""
        if not self.contains(item):
            self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def contains(self, item):
        """Проверка принадлежности элемента множеству."""
        return item in self._items

    def union(self, other):
        """Объединение: элементы, которые есть хотя бы в одном множестве."""
        result = self._new_empty()
        for item in list(self._items) + list(other._items):
            result.add(item)
        return result

    def intersection(self, other):
        """Пересечение: элементы, которые есть в обоих множествах."""
        result = self._new_empty()
        for item in self._items:
            if other.contains(item):
                result.add(item)
        return result

    def _new_empty(self):
        return MySet()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(list(self._items))

    def __contains__(self, item):
        return self.contains(item)

    def __str__(self):
        return "{" + ", ".join(str(item) for item in self._items) + "}"
