
import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_info(self):
        print("Длинна прямоугольника:", self.length, '\n'
              "Ширина прямоугольника:", self.width,)

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_square(self):
        print("Площадь прямоугольника:", self.length * self.width)

    def set_perimeter(self):
        print("Периметр прямоугольника", 2 * (self.length + self.width))

    def set_hypotenuse(self):
        res = round(math.sqrt(self.length**2 + self.width**2), 2)
        print("Гипотенуза прямоугольника", res)

    def rectangle_image(self):
        # print()
        for i in range(self.width):
            print('* ' * self.length,)


rec1 = Rectangle(9, 3)
# rec1.set_length(3)
# rec1.set_width(9)
rec1.print_info()

rec1.set_square()
rec1.set_perimeter()
rec1.set_hypotenuse()
rec1.rectangle_image()
