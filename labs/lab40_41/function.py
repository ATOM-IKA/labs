class Function:
    def __init__(self, name):
        self._name = name
        print("Вызван конструктор Function")

    @property
    def name(self):
        return self._name

    def value(self, x):
        raise NotImplementedError

    def derivative(self):
        raise NotImplementedError

    def info(self):
        print("Функция", self._name)
