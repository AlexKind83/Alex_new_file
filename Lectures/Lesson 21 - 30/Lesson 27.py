"""Разбираем тему Наследование ООП
   self._name Одно подчеркивание применяется для переменных которые используем внутри класса,
   за пределами класса оно будет подчеркиваться.
   Двойное подчеркивание self.__name разрешает использовать переменную внутри класса,
   в котором оно было создано.
   Делаем проверки.
   Смотрим класс(list), разбираем перегрузку методов, абстрактные методы."""
# Урок 27


# class Point:  # class Point(object)  применялось раньше
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# print(issubclass(Point, object))
# print(issubclass(Point, int))

# --------------------------------------------------------------------------------------------

# class Point:  # class Point(object)  применялось раньше
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Line:
#     """# ep: Point После двоеточия указывается рекомендуемый метод. \n
#        Если есть width=1 параметр по умолчанию, тогда не обязательно ставить двоеточие. \n"""
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     # def drew_line(self) -> str:
#     #     """ -> str указывает тип возвращаемого значения
#     #     (создано для тех кто использовал строгого типизированного языком"""
#     #     return f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self.width}"
#
#     def drew_line(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self.width}")
#
#
# class Rect:
#
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def drew_rect(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self.width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), 'yellow', 5)
# line.drew_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.drew_rect()

# Dru (Don't Repeat Yourself) не повторяйся

# -------------------------------------------------------------------------------------

# """Если 2 класса повторяются"""
# """Здесь посмотрели разницу с двойным подчеркиванием"""
#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         """Здесь посмотрели разницу с двойным подчеркиванием"""
#         return self.__width
#
#
# class Line(Prop):
#     def drew_line(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def drew_rect(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20), 'yellow', 5)
# line.drew_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.drew_rect()

# ---------------------------------------------------------------------------------------------
# """Можно и в дочернем класса создать инициализатор __init__"""
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор базового класса Prop")
#
#     def get_width(self):
#         """Здесь посмотрели разницу с двойным подчеркиванием"""
#         return self.__width
#
#
# class Line(Prop):
#     """Здесь создаем инициализатор дочернего класса. \n
#        Пример super() - ключевое слова обращения к родительскому классу"""
#     def __init__(self, *args):
#         super().__init__(*args)  # Prop.__init__(self, *args)
#         print("Переопределенный инициализатор Line")
#
#     def drew_line(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def drew_rect(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20), 'yellow', 5)
# line.drew_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.drew_rect()

# -------------------------------------------------------------------------------------

# """Хоти создавать много разных фигур, но используем только один параметр"""
#
#
# class Figure:
#
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.color = c
#
#
# class Rectangle(Figure):
#
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         super().__init__(color)
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Некорректное значение ширины")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Некорректное значение высоты")
#
#     def area(self):
#         """Получаем площадь прямоугольника"""
#         print(f"Площадь {self.color} прямоугольника = ", end='')
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.area())


# """Делаем проверки"""
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# """Создаем Родительский класс, и даем доступ дочернего класса к родительскому"""
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть быть числами")
#
#
# class Line(Prop):
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны целочисленными значениями")
#
#     def drew_line(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def drew_rect(self):
#         print(f"Рисование линий: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10,20), 'yellow', 5)
# line.set_coord(Point(15.5, 45), Point(100, 200))
# line.drew_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.set_coord(Point(55.5, 45.6), Point(100, 200))
# rect.drew_rect()


# #
# #
# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         """Чтобы не перезаписать метод родительского класса
#            надо добавить super().show_rect()"""
#         super().show_rect()
#         print('Фон:', self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, size, frame, color):
#         super().__init__(width, height)
#         self.size = size
#         self.frame = frame
#         self.color = color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.size} {self.frame} {self.color}')
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, '1px', 'solid', 'red')
# shape2.show_rect()


# #
# """Можно в класс передать данные типа список class Vector(list)"""
# """Здесь мы наследовались от класса List и у его своих много методов
#    и с ними нельзя применять __init__"""


# class Vector(list):
#     """Тут мы его переопределили в строку ' '.join(map(str, self))"""
#     def __str__(self):
#         return ' '.join(map(str, self))  # Тут мы его переопределили в строку
#
#
# v = Vector([1, 2, 3])
# print(sum(v))
# print(v)
# print(type(v))


# #
# """Перегрузка методов"""
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     # def set_coord(self, sp, ep=None):
#     #     """Здесь мы видоизменили код ep=None
#     #        и добавили проверку if ep is None: \n
#     #        Также можно сделать и с первым параметром,
#     #        только все будет проходить с дополнительной проверкой elif"""
#     #     if ep is None:
#     #         if sp.is_int():
#     #             self._sp = sp
#     #         else:
#     #             print("Координаты должны быть целочисленными значением")
#     #     else:
#     #         if sp.is_int() and ep.is_int():
#     #             self._sp = sp
#     #             self._ep = ep
#     #         else:
#     #             print("Координаты должны быть целочисленными значениями")
#
#     def set_coord(self, sp=None, ep=None):
#         if sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными значением")
#
#         elif ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координаты должны быть целочисленными значением")
#
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными значениями")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(15, 45), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(55, 55))
# line.draw_line()
# line.set_coord(ep=Point(77, 77))
# line.draw_line()


"""Абстрактные методы"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_digit(self):
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            return True
        return False

    def is_int(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coord(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть числами")

    def draw(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод draw()")


class Line(Prop):
    def draw(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Rect(Prop):
    def draw(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Ellipse(Prop):
    def draw(self):
        print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")


figs = list()
figs.append(Line(Point(0, 0), Point(10, 10)))
figs.append(Line(Point(10, 10), Point(20, 10)))
figs.append(Rect(Point(50, 50), Point(100, 100)))
figs.append(Ellipse(Point(-10, -10), Point(10, 10)))

for f in figs:
    f.draw()
