""" Абстрактный метод при его вызове, требует создание реализаций абстрактного метода
    в Дочернем классе.
    """
# Урок 28

# """Абстрактные классы"""
#
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         """Родительский абстрактный метод. \n
#            Можно оставить его пустым pass"""
#         print("Метод move() в базовом классе ")
#
#
# class Queen(Chess):
#     def move(self):
#         """Реализован абстрактный метод в дочернем классе"""
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()


# # Задача
# #
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} RUB")  # :.2f
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     SUFFIX = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.SUFFIX, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     SUFFIX = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.SUFFIX, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# # for elem in d:
# #     elem.print_value()
# #     # print(f" = {elem.convert_to_rub():.2f} RUB")  # :.2f
# #     elem.show()
# #
# # for elem in e:
# #     elem.print_value()
# #     elem.show()
#
# for elem in (d + e):
#     elem.print_value()
#     elem.show()


# # """Интерфейсы"""
# # """Интерфейсы состоят только из абстрактных методов"""
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild')
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# """Вложенные классы"""

# def outer():
#     a = 5
#
#     def inner():
#         print(a)
#     inner()
#
#
# outer()


# #  Вложенный клас разбираемся
# #
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def static_method():
#         print("Статический метод")
#
#     def outer_method(self):
#         print("Метод в наружном классе")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Вложенный класс", MyOuter.age, self.obj.name)
#             MyOuter.static_method()
#             self.obj.outer_method()
#
#
# out = MyOuter('Внешний')
# inner = out.MyInner('Внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# # Обращаемся к динамическим свойствам Родительского класса, вызывая метод Дочернего класса
# #
# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Color()
# outer.show()
# outer.lg.display()
#
# g = outer.lg
# g.display()


# Разбираем вложенные классы и наружные, и получаем к ним доступ
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#
#         def display(self):
#             print('Name:', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d1.display()
#
# d2 = outer.head
# d2.display()

# 2-----------------------------------------------------------------------------------------
# class Intern:
#     def __init__(self):
#         self.name = 'Smith'
#
#     def display(self):
#         print('Name:', self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d1.display()
#
# d2 = outer.head
# d2.display()


# Многоуровневые вложенные классы
#
# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Outer')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner")
#
#         class InnerClass:
#
#             def show(self):
#                 print('InnerClass')
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# # inner2 = inner1.inner_inner
# inner2 = outer.inner.inner_inner
# inner2.show()


# # Создаем Многоуровневые вложенные классы, только обращаемся через имя класса
# # и тогда не нужно будет создавать динамические свойства в Родительском классе
# #
# class Computer:
#     def __init__(self):
#         """Можно не создавать
#            self.os = self.OS()
#            self.cpu = self.CPU()"""
#         self.name = 'PC001'
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# """Магические методы"""

#
#
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


cat = Cat('Пушок')
print(cat)

cat = [Cat('Пушок')]
print(cat)
