'''
Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''


class Fabric:
    def __init__(self, kind, name, age, an_t: str, **kwargs):
        self.an_t = an_t
        self._kind = kind
        self._name = name
        self._age = age

        for key, value in kwargs.items():
            if key == 'kind':
                self.kind = value
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'spec':
                self.spec = value
            if key == 'size':
                self.size = value

    def get_an(self):
        if self.an_t == 'bird':
            return Birds(self._kind, self._name, self._age, self.color)
        elif self.an_t == 'mammal':
            return Mammals(self._kind, self._name, self._age, self.spec)
        elif self.an_t == 'fish':
            return Fishes(self._kind, self._name, self._age, self.size)
        else:
            return f'такого животного нет'


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


if __name__ == '__main__':
    animal1 = Fabric(an_t='bird', kind='птица', name='ворона', age=3, color='серая').get_an()

    class_name = type(animal1).__name__
    print("Class name:", class_name)
