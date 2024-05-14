import math


class Table:
    """Родительский класс \n
       Содержит метод исключения, для дочернего класса info_square_table"""
    def __init__(self, width, length, radius):
        self._width = width
        self._length = length
        self._radius = radius

    def info_square_table(self):
        raise NotImplementedError("В дочернем классе должен присутствовать метод square_table()")


class TableRectangular(Table):
    def square_table(self):
        """Подсчитывает площадь прямоугольного стола"""
        return self._width * self._length

    def set_square_table(self, width=None, length=None):
        """Применен метод перегрузки для параметров ширины, длинны."""
        if width is None:
            if length:
                self._length = length

        elif length is None:
            if width:
                self._width = width

        else:
            if width and length:
                self._width = width
                self._length = length

    def info_square_table(self):
        print(f"Площадь прямоугольного стола: {self.square_table()}")


class TableRound(Table):
    def square_table(self):
        """Подсчитывает площадь круглого стола"""
        return round(math.pi * (self._radius ** 2), 2)

    def info_square_table(self):
        print(f"Площадь круглого стола: {self.square_table()}")


rec = TableRectangular(20, 10, 0)
rec.info_square_table()
rec.set_square_table(length=20)
rec.info_square_table()
ro = TableRound(0, 0, 20)
ro.info_square_table()
