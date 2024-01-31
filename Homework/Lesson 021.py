def count_negative_numbers(lst):
    """\n
    if: return - возвращаем нуль, иначе вернувшее значение сложится со значением в блоке else \n
    elif: Если не сделать сдвиг индекса, то итерация будет бесконечной \n
    elif: return - Вызываем, функцию со сдвигом индекса[1] \n
    else: return - возвращаем в стек значение 1, и вызываем функцию со сдвигом индексах[1]
    """
    if len(lst) == 0:
        count = 0
        return count
    elif lst[0] > 0:
        return count_negative_numbers(lst[1:])
    else:
        count = 1
        # print(count)
        return count + count_negative_numbers(lst[1:])


print("n =", count_negative_numbers([-2, 3, 8, -11, -4, 6, -1]))
