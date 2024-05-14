user_number = tuple(input("Введите любые числа, без пробелов: "))
print(user_number)
b = ()

for i in user_number:
    # print(i, end=' ')
    # print(user_number.count(i), end=' ')
    if i not in b:
        b += tuple(i)
        # print(b)
        # print(i)
        print('Количество ', i, '=', user_number.count(i))
