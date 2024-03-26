"""Метод __call__(self, *args, **kwargs) делает перегрузку круглых скобок
   Метод __call__ рассчитан для создание декораторов класса"""
# Урок 31

"""Функторы"""


# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()  # происходит перегрузка иза метода __call__, и начинает идти подсчет
# c1()
# c1()
#
# c2 = Counter()
# c2()
# c2()
# c2()
#
# c1()  # идет подсчет дальше


"""Подходим потихоньку к классу декоратору"""
# # 2 2 примера (1 класс) (2 функция, с замыканием)
# #
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!; ")
# print(s1(" ?Hello World!!!!!  "))
#
#
# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars("?:!; ")
# print(s2(" ?Hello World!!!!!  "))

# ------------------------------------------------------------------
# 2 вариант


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, strings):  # Заменили параметры
#         if not isinstance(strings, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return strings.strip(self.__chars)
#
#
# s1 = StripChars("?:!; ")
# print(s1(" ?Hello World!!!!!  "))
#
#
# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars("?:!; ")
# print(s2(" ?Hello World!!!!!  "))


# Тут явный пример как класс выступает в роли декоратора
#
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("Перед вызовом функций")
#         self.func()
#         print("После вызова функций")
#
#
# @MyDecorator
# def function():
#     print("Текст функций")
#
#
# function()

# -----------------------------------------------------------------

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):  # добавляем, чтобы работал декоратор в функций
#         print("Перед вызовом функций")
#         res = self.func(x, y)
#         print("После вызова функций")
#         return res
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# ----------------------------------------------------------------------------------

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         # print("Перед вызовом функций")
#         # res = self.func(x, y)
#         # print("После вызова функций")
#         return f"Перед вызовом функций\n{self.func(x, y)}\nПосле вызова функций"
#
#
# @MyDecorator
# def function(a, b):
#     return a * b  # Если тут return, то в, функций должен быть return (также с print)
#
#
# print(function(2, 5))


# # Задача
# #
# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         return self.func(x, y) ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# Вернулись к рассмотрению.
# Добавили 3 параметр.

# class MyDecorator:
#     def __init__(self, func):
#         self.name = func
#
#     def __call__(self, *args):  # если не хотим привязываться к количеству аргументов
#         return f"Перед вызовом функций\n{self.func(*args)}\nПосле вызова функций"
#
#
# @MyDecorator(" два параметра")
# def function(a, b):
#     return a * b
#
#
# @MyDecorator( "три параметра")
# def function1(a, b, c):
#     return a * b * c
#
#
# print(function(2, 5))
# print(function1(2, 5, 2))

# --------------------------------------------------------------------------------------
# (добавляем параметры декоратора)

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f"Перед вызовом функций ({self.name})\n{func(*args, **kwargs)}\nПосле вызова функций"
#
#         return wrap
#
#
# @MyDecorator(" два параметра")
# def function(a, b):
#     return a * b
#
#
# @MyDecorator( "три параметра")
# def function(a, b, c):
#     return a * b * c
#
#
# print(function(2, 5))
# print(function(2, 5, 2))


# # Задача
# # с параметрами декоратора
# class Power:
#     def __init__(self, num):
#         self.num = num
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f"Результат: {func(*args, **kwargs) ** self.num}\n"
#
#         return wrap
#
#
# @Power(3)
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# """Декорирование метода"""
#
#
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('-' * 20)
#         fn(*args, **kwargs)
#         print('-' * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# """Декорация класса"""
#
#
# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


"""Дескрипторы"""

# Подходим к Дескриптору


# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         else:
#             self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         else:
#             self.__surname = value
#
#
# p =Person('Ivan', 'Petrov')
#  # p.name = 54


# ---------------------------------------------------------------------
# # Используем Дескриптор.
# # Убирает применения @property
#
# class String:
#     def __init__(self, value=None):
#         print(f"Инициализатор String {value}")
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError(f"{value} должно быть строкой")
#     #     else:
#     #         self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError(f"{value} должно быть строкой")
#     #     else:
#     #         self.__surname = value
#
#
# p =Person('Ivan', 'Petrov')
# # p.name.set(54)


"""Дескриптор методы: (__get__, __set__, __delete__, __set_name__)"""
"""Стандартный синтаксис записи"""


class ValidString:  # Дескриптор
    def __set_name__(self, owner, name):  # 2 аргумента обязательно, но не обязательно его выводить
        print(owner)  # Не обязательный
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.__name} должно быть строкой")
        instance.__dict__[self.__name] = value


class Person:
    name = ValidString()
    surname = ValidString()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


p = Person('Ivan', 'Petrov')
# p.name = 5
print(p.name)
print(p.surname)
print(p.__dict__)

