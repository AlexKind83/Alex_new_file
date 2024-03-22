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

    @staticmethod
    def check(other):
        """Исключение для Перегрузки операторов. \n
           Служит для проверки правого операнда, что он является типом класса Clock."""
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом класса Clock")

    def __add__(self, other):
        self.check(other)
        # if not isinstance(other, Clock):
        #     raise ArithmeticError("Правый операнд должен быть типом класса Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        self.check(other)
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        self.check(other)
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        self.check(other)
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        self.check(other)
        return Clock(self.sec % other.sec)


c1 = Clock(10_000)
c2 = Clock(4_000)
print(c1.get_format_time())
print(c2.get_format_time())

c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
c6 = c1 // c2
c7 = c1 % c2

print()
print(f'{c3.get_format_time()} (x + y)')
print(f'{c4.get_format_time()} (x - y)')
print(f'{c5.get_format_time()} (x * y)')
print(f'{c6.get_format_time()} (x // y)')
print(f'{c7.get_format_time()} (x % y)')
