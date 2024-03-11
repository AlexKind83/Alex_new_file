class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Ошибка")

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Некорректно")

    @age.deleter
    def age(self):
        del self.__age


p1 = Person('Irina', 26)
print(p1.__dict__)
p1.name = 'Igor'
p1.age = 31
print(p1.name)
print(p1.age)
# del p1.name
print(p1.__dict__)
del p1.age
print(p1.__dict__)