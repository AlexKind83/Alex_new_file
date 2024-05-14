def decor(fn):
    def wrap(*args):
        """
        Функция содержит аргумент, возвращенный функцией "number_sum".
        Внимание:

        *args = общая сумма

        args = картеж
        """
        x = fn(*args) / len(args)
        print("Среднее арифметическое:", x)

    return wrap


@decor
def number_sum(*args):
    """
    В 18 строку приходит кортеж из 4 чисел.
    В 23 строке мы складываем картеж, и получаем число со значением int.
    """
    x = sum(args)
    print("Сумма чисел:", x)
    return x


number_sum(2, 3, 3, 4)
