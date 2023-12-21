
import math

footing = int(input("Введите основание: "))
height = int(input("Введите высоту: "))
radius = int(input("Введите радиус: "))


def rectangle(a, b):
    return a * b


def triangle(a, b):
    return (a * b) / 2


def circle(r):
    return math.pi * (r ** 2)


res_1 = rectangle(footing, height)
print("\nПлощадь прямоугольника:", res_1)

res_2 = triangle(footing, height)
print("Площадь треугольника:", res_2)

res_3 = circle(radius)
print("Площадь круга:", res_3)
