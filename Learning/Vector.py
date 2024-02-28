import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """Отвечает что будет, выводится в консоли. \n
        В данном случае выведется Vector(x, y). \n
        Без __repr__  будет выводится __main__.Vector object at 0x0000024CB414FD00>"""
        return f"Vector({self.x},{self.y})"

    def __abs__(self):
        """Данный пример выводит гипотенузу \n
        Если один x - x**2 \n
        Если x, y - (x * x) + (y * y)"""
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        """Делает + - * /, или любой другой оператор \n
           Данный пример делает сложение между v1.x + v2.x \n
           И точно такое-же действие происходит и с y
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """Содержит скаляр, который выводит выражено одним числом. \n
           По теореме Пифагора a*2 + b*2 = c*2 и разделено на степень"""
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v3 = Vector(3, 4)
print(abs(v3))

print(v3 * 3)
print(abs(v3 * 3))
