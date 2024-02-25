"""Узнаем @classmethod.
   Применяем @classmethod и @staticmethod.
   2 большие задачи.
   1 Создаем подсчет.
   2 нацелена на полный разбор проверок """

# Урок 26

# 1 Переменную с помощью map() разбили, и в класс дали переменные.
#
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# string_date = "23.10.2024"
# day, month, year = map(int, string_date.split('.'))  # Таким способом дали данные переменным в класс
# # print(day, month, year)
# date = Date(day, month, year)
# print(date.string_to_db())


# # 2 Создаем @classmethod и переносим в его (1) (2)
#
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod  # (3) Создаем переменные класса (явное преобразование типов)
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))  # (1)
#         date1 = cls(day, month, year)  # (2) промежуточный можно не писать, а написать return cls(day, month, year)
#         return date1  # можно и так cls(day, month, year)
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# date2 = Date.from_string("23.10.2024")  # (3)
# print(date2.string_to_db())
# date3 = Date.from_string("25.12.2023")
# print((date3.string_to_db()))
#
# # string_date = "23.10.2024"
# # day, month, year = map(int, string_date.split('.'))  # (1)
# # date = Date(day, month, year)  # (2)
# # print(date.string_to_db())


# # 3 Проверяем на корректность, чтобы не было ошибок.
# #
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod  # Делаем проверку методу класса который выше (чтобы не было ошибок)
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999  # Возвращаем с условием
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2024',
#     '12.31.2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print("Неправильная дата или формат строки с датой")

# date2 = Date.from_string("23.10.2024")
# print(date2.string_to_db())
# date3 = Date.from_string("25.12.2023")
# print((date3.string_to_db()))


# # Задача
# #
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod  # Переписываем статический метод (rate_usd = 0.013)
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod  # # Переписываем статический метод (rate_eur = 0.011)
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете")
#         print('-' * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         """Обратить внимание {self.percent:.0%} тут после точки идет 0 значений"""
#         print(f"Проценты: {self.percent:.0%}")  # здесь применили возможности self
#         print('-' * 20)
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)
# acc.print_info()
# acc.print_balance()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
#
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_percent()
#
# print()
# acc.withdraw_money(100)
#
# print()
# acc.withdraw_money(3000)
#
# print()
# acc.add_money(5000)
#
# print()
# acc.withdraw_money(3000)


#


# # Рассматриваем разные способы проверки инициализаций
# #
import re


class UserData:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)  # проверка вынесена сюда, чтобы предусмотреть корректный ввод данных
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__fio = fio
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def password(self):
        return self.__ps

    @password.setter
    def password(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("Ф.И.О. должны быть строкой")
        f = fio.split()  # ['Волков2', 'Иго8рь', 'Николаевич&']
        if len(f) != 3:
            raise TypeError("Не верный формат Ф.И.О.")
        letters = ''.join(re.findall('[a-zа-яё-]', fio, re.IGNORECASE))  # (3)
        for s in f:
            if len(s.strip(letters)) != 0:
                raise TypeError("В Ф.И.О. можно использовать только буквы и дефис")
        """(3) Код который можно написать 3 вариант проверки"""
        # re.findall(r'{^a-zа-яё\s-]', re.IGNORECASE)

    @staticmethod
    def verify_old(old):
        if not isinstance(old, int) or old < 14 or old > 65:  # или 14 < old < 65
            raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 65 лет")

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()  # ['1234', '567890']
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")


p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.0)
p1.fio = "Волков Игорь Викторович"
print(p1.fio)


# 2 Здесь private убираем
# И инициализация проверок проходит через setter
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)  # проверка вынесена сюда, чтобы предусмотреть корректный ввод данных
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("Ф.И.О. должны быть строкой")
#         f = fio.split()  # ['Волков2', 'Иго8рь', 'Николаевич&']
#         if len(f) != 3:
#             raise TypeError("Не верный формат Ф.И.О.")
#         letters = ''.join(re.findall('[a-zа-яё-]', fio, re.IGNORECASE))  # (3)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В Ф.И.О. можно использовать только буквы и дефис")
#         """(3) Код который можно написать 3 вариант проверки"""
#         # re.finball(r'{^a-zа-яё\s-]', re.IGNORECASE)
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 65:  # или 14 < old < 65
#             raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 65 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.0)
# p1fio = "Волков Игорь Викторович"
# print(p1.fio)

