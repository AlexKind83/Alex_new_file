# Урок 2


# num1 = 4321
# print("Исходное число:", num1)
# a = num1 / 10
# num1 //= 10
# b = num1 % 10
# num1 //= 100
# print(a)
# print(b)

# num1 = 4325
# print("Исходное число", num1)
# res = num1 % 10 * 1000
# num1 //= 10
# res += num1 % 10 * 100
# num1 //= 10
# res = num1 % 10 * 10
# num1 //= 10
# res += num1 % 10
# print(res)


# num1 = "2"
# num2 = 3
# # res = num1 + str(num2)
# res = int(num1) + num2
# print(res)


# print(int(3.8))
# print(round(3.543))
# print(type(round(3.543)))
# print(round(3.543, 2))
# print(type(round(3.543, 2)))
# print(round(3.595, 2))
# print(type(round(3.595, 2)))


# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)
# res = float(num1) + num2
# res = round(res)
# print(res)


# name = "Виктория"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="---")
# print("Меня зовут", name + ". Мне", age, "лет.", sep=" ", end=" ")
# print("Я учу Python.")
# print("Меня зовут", name + ". Мне", age, "лет.", sep=" ", end="\n\n")
# print("Я учу Python.")
# print("Меня зовут", name + ". Мне", age, "лет.", sep=" ", end="--//--")
# print("Я учу Python.")


# name = input("Введите имя: ")
# print(name)


# num = input("Введите число: ")
# # print(num)
# # print(type(num))
# power = input("Введите степень: ")
# res = int(num) ** int(power)
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# num = input("Введите число: ")
# power = input("Введите степень: ")
# num = int(num)
# res = int(num) ** int(power)
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))


# # Не явное преобразование типов
# b1 = True
# b2 = False
# print(b1 + 5)  # 1 +5
# print(b2 + 5)  # 0 + 5

# False => "", 0, False, None

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)


# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print(9 >= 9)
# print("привет" > "ПРИВЕТ")


# print(2 < 4 < 9)  # 2 < 4 < 9 => True && True => True
# print(2 * 5 > 7 >= 4 + 5)  # True && True => True
# print(3 * 5 <= 7 >= 2)  # False && True => False


# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False


# and означает и
# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False:False)


# # or означает или
# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False:False)


# # not означает не
# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)


# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)
#
# cnt1 = 5    # Может быть такой код (но он не приветствуется)
# if cnt1 < 10: cnt1 += 2; print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")


# side1 = int(input("Введите сторону 1: "))
# side2 = int(input("Введите сторону 2: "))
# side3 = int(input("Введите сторону 3: "))
# if user1 == user2 == user3:
#     print("Треугольник равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник равнобедренный")


#              # Как упростить код ввода диапазона

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ")
# elif day == 6 or day == 7:
#     print("Выходной день - ")
# else:
#     print("Такого дня недели не существует")

#           # 2 вариант
#           # расписывает каждый день

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

