import random


def tuple_value():
    a = tuple(random.randrange(0, 5) for _ in range(10))
    print(a)
    b = tuple(random.randrange(-5, 1) for _ in range(10))
    print(b)
    c = a + b
    print(c)
    return c


tuple_res = tuple_value().count(0)
print('0 =', tuple_res)
