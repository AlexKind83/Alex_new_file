"""__slots__ экономит место, и за того что фиксирует память.
   __slots__
   Множественное наследование"""

# Урок 29


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))


#
#
# import geometry


# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = geometry.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(1, 2)
# print(p.length)
# p.length = 20
# print(p.length)

# ------------------------------------------------------------

# class Point:
#     __slots__ = ('x', 'y')  # __slots__ экономит место, и за того что фиксирует память
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
# print('pt1 =', pt1.__sizeof__())
# print('pt2 =', pt2.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())
# print(pt2.__dict__)
# # print(pt1.__dict__)  # Вызовет ошибку и за закрытых Атрибутов с помощью __slots__

# ------------------------------------------------------------------------------------


# class Point:
#     __slots__ = ('x', 'y')  # Теряет свой смысл если не указан в Родительском классе
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt1 = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)


"""Множественное наследование"""


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is player")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog('Buddy')
# dog.bark()
# dog.play()
# dog.sleep()


# # Используем одинаковые имена Методов
#
#
# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#     def hi(self):
#         print('A')
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#     def hi(self):
#         print('B')
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#     def hi(self):
#         print('C')
#
#
# class D(B, C):
#     def __init__(self):
#         C.__init__(self)
#         B.__init__(self)
#         print("Инициализатор класса D")
#
#
# d = D()
# d.hi()
# print(D.mro())  # Метод для проверки иерархий последовательности классов ( __mro__ )

# -----------------------------------------------------------------------------------

# Делаем разветвление классов.
# Было D -> B -> C - A.
# Стало 1 ветка D -> B - A  (2 ветка D -> C -> A)
# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#     def hi(self):
#         print('A')
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса АA")
#
#     def hi(self):
#         print('AA')
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#     def hi(self):
#         print('B')
#
#
# class C(AA):  # Добавили вместо класса А, класс АА
#     def __init__(self):
#         print("Инициализатор класса C")
#
#     def hi(self):
#         print('B')
#
#
# class D(B, C):
#     def __init__(self):
#         C.__init__(self)
#         B.__init__(self)
#         print("Инициализатор класса D")
#
#
# d = D()
# d.hi()
# print(D.mro())


# Здесь классы идут по, иерархий (по цепочке)
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pas:
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         print("Инициализатор класса Pas")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(color, width)  # Приобрел данные класса Styles(обязательно чтобы перейти в класс Styles)
#
#
# class Line(Pas, Styles):
#     def draw(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.__mro__)


# -------------------------------------------------------------------------------------
# # Если родительский элемент меняем, то ломается иерархия построения классов
# # Его желательно использовать только когда наследуется от одного Родительского класса
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class Pas(A):  # Ломаем иерархию построение цепочки классов
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         print("Инициализатор класса Pas")
#         self._sp = sp
#         self._ep = ep
#         Styles.__init__(self, color, width)
#         # super().__init__(color, width)  # Приобрел данные класса Styles(обязательно чтобы перейти в класс Styles)
#
#
# class Line(Pas, Styles):
#     def draw(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.__mro__)


"""Класс Миксины"""
# Его применяют как добавления Атрибутов


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a', encoding='UTF-8') as fn:
#             fn.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='sublog.txt')
#
#
# subclass = MySubClass()
# subclass.display("Строка будет отображаться и запишется в файл \n")
# print(MySubClass.__mro__)


#
#
# class Goods:
#     def __init__(self, name, weight, price):
#         print("Инициализатор класса Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()  # указываем обращение к последующей иерархий класса(обязательно чтобы работало)
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Инициализатор класса MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NotBook(Goods, MixinLog):
#     pass
#
#
# n = NotBook("Intel", 1.5, 35_000)
# n.print_info()
# n.save_sell_log()
# print(NotBook.__mro__)


"""Перегрузка операторов"""
# # 24 * 60 * 60 = 86_400 - число секунд в одном дне
#
#
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
#
# c1 = Clock(60)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 + c2
# print(c3.get_format_time())
#
# c2 += c1
# print(c2.get_format_time())
