import os

text = "Постоянное время: О(1) \nЛинейное время: О(n) \nКвадратичное время: О(n**2) \nКубическое время: О(n**3) \n"
my_file = r"..\Learned lesson 21 - 30\Task 22.txt"


def replacing_lines(files, st):

    if not os.path.isfile(files):
        with open(files, 'w') as f:
            f.write(st)

    with open(my_file, 'r') as f1, open(my_file, 'r') as f2:
        ls = f1.readlines()
        print(f2.read())

    poss_1 = int(input("Введите строку от 0 до 3, которую хотите заменить: "))
    poss_2 = int(input("Введите 0 до 3, заменяемую строку: "))

    if 0 <= poss_1 | poss_2 <= len(ls):
        ls[poss_1], ls[poss_2] = ls[poss_2], ls[poss_1]
    else:
        print('-' * 50)
        print("Введен не корректно номер строки!\nДиапазон строк идет от 0 до 3")
        print('-' * 50)
        return replacing_lines(files, st)

    with open(my_file, 'w') as f:
        f.writelines(ls)
        print()
        print(ls)


replacing_lines(my_file, text)
