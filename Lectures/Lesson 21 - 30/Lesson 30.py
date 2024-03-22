""""""

# Урок 30

"""Перегрузка операторов"""


class Clock:
    DAY = 86_400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом класса Clock")
        return Clock(self.sec + other.sec)

    # def __eq__(self, other):  # (1) делаем сравнение чтобы отработал оператор равенства
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом класса Clock")
    #     return self.sec == other.sec

    # def __ne__(self, other):
    #     return not self.__eq__(other)  # (2) Если не хотим писать заново, то что в методе __eq__

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом класса Clock")
        return self.sec < other.sec

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом класса Clock")
        return self.sec <= other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом класса Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом класса Clock")
        return self.sec >= other.sec


c1 = Clock(200)
c2 = Clock(200)
print(c1.get_format_time())
print(c2.get_format_time())
c3 = c1 + c2
print(c3.get_format_time())
c4 = c1 + c3
print(c4.get_format_time())

# if c1 == c2:  # (1)
#     print("Время равно")
# else:
#     print("Время разное")

# if c1 > c2:
#     print("+")
# else:
#     print('-')

# print(f'c1 < c2: {c1 < c2}')
# print(f'c1 <= c2: {c1 <= c2}')
# print(f'c1 > c2: {c1 > c2}')
# print(f'c1 >= c2: {c1 >= c2}')


#
#
# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):  # создаем промежуточные переменные(если хотим выйти за диапазон индекса)
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым положительным числом")
#         if not 0 <= key < len(self.marks):
#             raise IndexError("Индекс за пределом диапазона")
#         del self.marks[key]
#
#
# s1 = Student('Сергей', 5, 6, 3, 4, 7)
# # print(s1.name)
# # print(s1.marks[2])
# # print(s1[2])
# # s1[2] = 8
# # print(s1[2])
# # print(s1.marks)
#
# s1[10] = 9
# print(s1.marks)
#
# del s1[3]
# print(s1[9])
# print(s1.marks)


# # Вернулись к первой задачи
# #
# class Clock:
#     DAY = 86_400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом класса Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):  # (1) делаем сравнение чтобы отработал оператор равенства
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом класса Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)  # (2) Если не хотим писать заново, то что в методе __eq__
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом класса Clock")
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         return not self.__lt__(other)
#
#     # def __getitem__(self, item):
#     #     if not isinstance(item, str):
#     #         raise ValueError("Ключ должен быть строкой")
#     #
#     #     if item == 'hour':
#     #         return (self.sec // 3600) % 24
#     #     if item == 'min':
#     #         return (self.sec // 60) % 60
#     #     if item == 'sec':
#     #         return self.sec % 60
#     #
#     #     return "Неверный ключ"
#
#     def __getitem__(self, item):  # (1)
#         """2 вариант лучше. \n
#            Он следует правилу не повторяйся!"""
#         hour_, min_, sec_ = self.get_format_time().split(':')
#         time_key = {
#             'hour': hour_,
#             'min': min_,
#             'sec': sec_,
#         }
#         try:
#             return time_key[item]
#         except KeyError:
#             raise ValueError("Ключ должен быть строкой")
#
#     def __setitem__(self, key, value):  # (2)
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Ключ должен быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3_600
#         if key == 'min':
#             self.sec = s + 60 * value + h * 3_600
#         if key == 'sec':
#             self.sec = value + 60 * m + h * 3_600
#
#
# c1 = Clock(80_000)
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])  # (1)
#
# c1['hour'] = 11  # (2)
# c1['min'] = 25
# c1['sec'] = 50
# print(c1['hour'], c1['min'], c1['sec'])
# print(c1.get_format_time())


# # Задача
# #
# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == 'M':
#             return f"{self.name} is good boy!!!"
#         elif self.pol == 'F':
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         """Создаем проверку, что от 2 М не может быть котят. \n
#            Присутствует рандом на количество котят"""
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(['M', 'F'])) for _ in range(randint(1, 3))]
#         else:
#             raise TypeError("Type are not supports")
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Elsa', 5, 'F')
# cat3 = Cat('Maison', 4, 'M')
# print(cat1)
# print(cat2)
# print(cat1 + cat2)
#
# print(cat3)
# # print(cat1 + cat3)


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimetr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)

s1 = Square(10)
s2 = Square(20)

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]

for g in shape:
    print(g.get_perimetr())

