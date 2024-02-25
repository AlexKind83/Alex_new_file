# Урок 24

# OOP
# В классе могут быть:
# свойства (поля, переменные)
# методы (функций)


# __dict__ выводит свойства класса


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(id(p1))
# p1.x = 5
# p1.y = 24
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)  # __dict__ Видит только измененные свойства класса
#
# p2 = Point()
# print(id(p2))
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
#
# print(id(Point))  # У класса и его содержимого разные id
#
# print(isinstance(p1, Point))  # Проверяем тип данных
# ------------------------------------------------------------------------


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self):  # self Ссылка на экземпляр класса
#         print(self.__dict__)
#
#
# p1 = Point()  # Создается экземпляр класса
# p1.x = 5
# p1.y = 24
#
# p1.set_coord()  # Частый используемый метод написания
# # Point.set_coord(p1)  # Такой способ используется редко
#
# p2 = Point()
# p2.x = 10
# p2.y = 30
#
# p2.set_coord()
# --------------------------------------------------------------------------


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):  # Передаем параметры в вызываемую функцию класса
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.set_coord(5, 24)
# Point.set_coord(p1, 5, 24)
#
#
# p2 = Point()
# p2.set_coord(10, 30)

# --------------------------------------------------------------------------------

# # Задача
#
# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     citi = 'citi'
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные  ".center(40, '*'))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.citi}\nДомашний адрес: {self.address}")
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, citi, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.citi = citi
#         self.address = address
#
#     def set_address(self, address):  # устанавливаем адрес
#         self.address = address
#
#     def get_address(self):  # получаем адрес
#         return self.address
#
#     def set_name(self, name):  # устанавливаем имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва',
#               'Чистопрудный бульвар, 1А')
# h1.set_address("ул. Ленина, 56")
# h1.print_info()
# h1.set_name('Юлия')
# print(h1.get_address())
# print(h1.get_name())



# # Задача
# #
# class Person:
#     skill = 10  # статическое свойства
#     name = ''
#     surname = ''
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print("Данные сотрудника: ", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person()
# p1.print_info("Виктор", "Резник")
# p1.add_skill(3)
#
# p2 = Person()
# p2.print_info("Анна", "Долгих")
# p2.add_skill(2)


# 2 вариант

# class Person:
#     skill = 10  # статическое свойства
#     name = ''
#     surname = ''
#
#    def __init__(self, name, surname):
#         self.name = name  # динамические свойства
#         self.surname = surname
#         print("Инициализация класса", self)
#
#     def __del__(self):  # Разрывает связь на определенный элемент
#         print("Удаления экземпляра", self)
#
#     def print_info(self):
#         print("Данные сотрудника: ", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1  # Разорвет связь только 1 экземпляр класса (2 не затронет)
#
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# # 3 добавляем (подсчитываем сколько экземпляров класса создано)
#
# class Person:
#     skill = 10  # статическое свойства
#     count = 0
#
#     def __init__(self, name, surname):
#         self.name = name  # динамические свойства
#         self.surname = surname
#         # self.count += 1  # будет выводить только 1
#         # обращаемся к самому классу
#         Person.count += 1  # Через имя класса обращаемся к свойству (он будет считать)
#
#     def print_info(self):
#         print("Данные сотрудника: ", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# print(p1.count)
#
# p2 = Person("Анна", "Долгих")
# print(p2.count)
#
# print()
# print(Person.count)


# # Задача
# #
# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается')
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
#
# print("Численность роботов:", Robot.k)
