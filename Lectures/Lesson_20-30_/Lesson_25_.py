"""Создаем закрытые свойства (статические и динамические) \n
   Получаем доступ к закрытым динамическим свойствам. \n
   Создаем проверки. \n
   Создаем закрытый экземпляр класса с условием, и подставляем закрытый экземпляр класса в другое условие. \n
   Применяем (__slots__) чтобы закрыть доступ к свойствам, в не поля класса. \n
   Создаем закрытые экземпляры класса, и получаем к ним доступ, с помощью старого метода property(). \n
   Применяем новый способ доступа к закрытым экземплярам класса, с помощью декоратора @property. \n
   Создаем закрытое статическое свойство, и получаем доступ к ним, старым и новым способом staticmethod. \n
   В статическом методе функция работает как ОБЫЧНАЯ функция. \n
   """

# Урок 25

# #
# #
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.x, p1.y)
# print(p1.__dict__)  # ПОСМОТРЕТЬ свойства
# p1.x = 100
# p1.y = 'abc'
# print(p1.x, p1.y)


# Модификаторы доступа
# public -
# protected -
# private -


# # Создаем проверку для вводимых x, y
# #
# class Point:
#     def __init__(self, x, y):
#         """Создаем закрытые свойства"""
#         self.__x = x  # private
#         self.__y = y  # private
#
#     def __check_value(parameter):  # За пределами класса нельзя обратится (закрытый экземпляр класса)
#         """Делаем экземпляр класса с условием \n
#         условие для set_coord"""
#         if isinstance(parameter, int) or isinstance(parameter, float):
#             return True
#         return False
#
#     def get_coord(self):  # Получить доступ (открытый метод)
#         """даем доступ к закрытым свойствам"""
#         return self.__x, self.__y  # Получаем доступ к private
#
#     def set_coord(self, x, y):  # Установить доступ (открытый метод)
#         """Созданная проверка \n
#         в 2 вариантах"""
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(100, 200)
# print(p1.get_coord())
# print(p1.__dict__)  # Смотрим свойства и видим что есть 2 служебное свойства
# # print(Point.__dict__)


# # # Добавляем проверку в __init__ чтобы при вводе данных уже проверялись данные
# #
# class Point:
#     def __init__(self, x, y):
#         """Проверяем на начальном этапе \n
#         если свойства не проходят проверку \n
#         они будут равны нулю"""
#         self.__x = self.__y = 0  # Если не пройдет проверку
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(parameter):
#         if isinstance(parameter, int) or isinstance(parameter, float):
#             return True
#         return False
#
#     # """убираем и делаем доступ отдельно к x и y"""
#     # def get_coord(self):
#     #     return self.__x, self.__y
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):  # Если нужен доступ к отдельному значению
#         return self.__x
#
#     def get_y(self):  # Если нужен доступ к отдельному значению
#         return self.__y
#
#
# p1 = Point('5', 10)
# p1.set_coord(100, 200)
# print(p1.__dict__)


# # Убираем проверку общею проверку на x, y, и делаем отдельную
# #
# class Point:
#     def __init__(self, x, y):
#         """Внесена отдельная проверка"""
#         self.__x = self.__y = 0  # Если не пройдет проверку
#         if Point.__check_value(x):
#             self.__x = x
#         if Point.__check_value(y):
#             self.__y = y
#
#     def __check_value(parameter):
#         if isinstance(parameter, int) or isinstance(parameter, float):
#             return True
#         return False
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата", x, "должны быть числом")
#
#     def get_y(self):
#         return self.__y
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата", y, "должны быть числом")
#
#
# p1 = Point("5", 10)
# # p1.set_coord("100", 200)
# print(p1.get_x())
# print(p1.get_y())
# print(p1.__dict__)


# Закрыть доступ за пределами класса с помощью __slots__
# Все что вносится в __slots__ будет работать, а что нет внесено не будет

# class Point:
#     """Добавлен __slots__ с разрешенными свойствами"""
#     __slots__ = ("__x", "__y", 'z')  # Закрываем доступ (все что здесь будет работать)
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x):
#             self.__x = x
#         if Point.__check_value(y):
#             self.__y = y
#
#    def __check_value(parameter):
#        if isinstance(parameter, int) or isinstance(parameter, float):
#            return True
#        return False
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата", x, "должны быть числом")
#
#     def get_y(self):
#         return self.__y
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата", y, "должны быть числом")
#
#
# p1 = Point("5", 10)
# print(p1.get_x())
# print(p1.get_y())
# p1. z = 100
# print(p1.z)


# # Убираем все лишнее.
# # Делаем все экземпляры класса закрытыми
# # используем старый вариант инициализаций закрытых экземпляров класса property(__get_x, __set_x)
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# print(p1.x)
# del p1.x
# # p1.x = 100
# print(p1.__dict__)


# # # Добавлен метод для получения доступа к закрытым экземплярам класса @property
# #
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if not isinstance(x, (int, float)):
#             raise TypeError("Устанавливаемое значение должно быть числом")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_y(self, y):
#         self.__y = y
#
#
# p1 = Point(5, 10)
# print(p1.x)
# p1.x = 100
# # print(p1.__dict__)


# ---------------------------------------------------------------------------------------------

# # Задача
# #
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.kg, 'кг => ', end='')
#         print(self.to_pounds(), 'фунтов')
#
#
# weight = KgToPounds(12)
# weight.print_data()
# print()
#
# print(weight.kg, 'кг => ', end='')
# print(weight.to_pounds(), 'фунтов')
# # weight.kg = 41  # Когда присваиваем новое значение отрабатывает set
# print(weight.kg, 'кг => ', end='')
# print(weight.to_pounds(), 'фунтов')
# weight.kg = 'десять'


# # Работа со статическими свойствами (private)
# #
# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod  # Даем понять что это статический метод
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)  # Старый способ для добавления статического метода и т.п.
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())


# # Добавление и вызов статического свойства (вызываются через имя класса)
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# # Задача
# #
# class Tools:
#     @staticmethod
#     def max(*args):
#         return max(args)
#
#     @staticmethod
#     def min(*args):
#         return min(args)
#
#     @staticmethod
#     def mubble(*args):
#         return sum(args) / len(args)
#
#     # Через рекурсию
#     # @staticmethod
#     # def factorial(num):
#     #     if num == 1
#     #         return 1
#     #     else:
#     #         return Tools.factorial(num - 1) * num
#
#     @staticmethod
#     def factorial(num):
#         fact = 1
#         for i in range(1, num + 1):
#             fact *= i
#         return fact
#
#
# print(f'Максимальное число: {Tools.max(3, 5, 7, 9)}')
# print(f"Минимальное число: {Tools.min(3, 5, 7, 9)}")
# print(f"Среднее арифметическое: {Tools.mubble(3, 5, 7, 9)}")
# print(f"Факториал числа: {Tools.factorial(5)}")


# # Задача
# #
from math import sqrt


class Square:
    __count = 0

    @staticmethod
    def square_triangle1(a, b, c):
        Square.__count += 1
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def square_triangle2(a, b):
        Square.__count += 1
        return 0.5 * a * b

    @staticmethod
    def square_area(a):
        Square.__count += 1
        return a * a

    @staticmethod
    def square_rectangle(a, b):
        Square.__count += 1
        return a * b

    @ staticmethod
    def get_count():
        return Square.__count

    def print_info(self):
        print(self, 'Hello')


print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
print('Площадь квадрата:', Square.square_area(7))
print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
print('Количество подсчетов площади:', Square.get_count())

print()
area = Square()
area.print_info()
area1 = Square()
Square.print_info(area1)


