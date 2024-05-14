"""@property используется для проверки, что приходит в экземпляр класса"""
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}"

    @staticmethod
    def check(other):
        """Исключение для Перегрузки операторов. \n
           Служит для проверки операндов, что он является типом класса Clock."""
        if not isinstance(other, Point3D):
            raise ValueError("Правый операнд должен быть типом класса Clock")

    def __add__(self, other):
        self.check(other)
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3D(x, y, z)
        # return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)  # или так

    def __sub__(self, other):
        self.check(other)
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point3D(x, y, z)

    def __mul__(self, other):
        self.check(other)
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Point3D(x, y, z)

    def __truediv__(self, other):
        self.check(other)
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Point3D(x, y, z)

    def __eq__(self, other):
        """Выводит каждому значению False, то что закомментировано. \n
           Выводит общий False."""
        self.check(other)
        # x = self.x == other.x
        # y = self.y == other.y
        # z = self.z == other.z
        return self.x == other.x and self.y == other.y and self.z == other.z
        # return Point3D(x, y, z)  # Лучше не применять имя класса

    def __getitem__(self, item):
        key = {'x': self.x,
               'y': self.y,
               'z': self.z}
        try:
            return key[item]
        except KeyError:
            raise ValueError("Ключ должен быть строкой")

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError(f"Ключ должен быть строкой")

        if not isinstance(value, int):
            raise TypeError(f"Значение должно быть числом")

        if key == 'x':
            self.x = value
        if key == 'y':
            self.y = value
        if key == 'z':
            self.z = value


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)

print(f"Координаты 1-й точки:", p1)
print(f"Координаты 2-й точки:", p2)
print()

p3 = p1 + p2
p4 = p1 - p2
p5 = p3 * p4
p6 = p3 / p4

print(f"Сложение координат:", p3)
print(f"Вычитание координат:", p4)
print(f"Умножение координат:", p5)
print(f"Деление координат:", p6)
print()

print(f"Равенство координат:", p1 == p2)
print()

print(f"x1 = {p1['x']}, x2 = {p2['x']}")
print(f"y1 = {p1['y']}, y2 = {p2['y']}")
print(f"z1 = {p1['z']}, z2 = {p2['z']}")

p2['x'] = 20
print(f"Запись значение в координату x2: {p2['x']}")

print(f"x1 = {p1['x']}, x2 = {p2['x']}")
