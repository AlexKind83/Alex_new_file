""""""
# Урок 32

# """Дескрипторы продолжаем"""


# Добавляем отдельную проверку, и применяем его в __set__
# (3) Изменяем применения Дескриптора только нужно изменить имя(обязательно)
# Второй вариант Дескриптора
#
# class Integer:
#
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord}  должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.__name = "_" + name  # (3) Тут мы при выводе имени добавили подчеркивание
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)  # (3) (1) это получить у экземпляра значение
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.__name] = value
#         setattr(instance, self.__name, value)  # (3) (2) instance = экземпляр класса, имя, значение
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.x = 20  # (2)
# print(p1.x)  # (1)
# print(p1.__dict__)


# """Метаклассы"""
#
#
# # a = 5
# # print(type(5))
# # print(type(int))  # Это мета класс на основе которого создан int
#
#
# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# print(lst, lst.get_length())
#
# # создаем мета класс
# MyList1 = type(
#     "MyList1",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst1 = MyList1()
# lst1.append(5)
# lst1.append(8)
# print(lst1, lst1.get_length())
#
# print(MyList.__dict__)
# print(MyList1.__dict__)


"""Создаем новые документы (модуль) и пакеты"""
# # geometry (пакет) Это папка в которой находятся модули (если указать в import только пакет, то он работать гне будет
# # rect1 (модуль)
# from geometry import rect32, sq32, trian32
# # from  geometry import *
#
#
# def run():
#     r1 = rect32.Rectangle(1, 2)
#     r2 = rect32.Rectangle(3, 4)
#
#     s1 = sq32.Square(10)
#     s2 = sq32.Square(20)
#
#     t1 = trian32.Triangle(1, 2, 3)
#     t2 = trian32.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()


# ----------------------------------------------------------------------------
# Задача (про пакеты и модули)
#
# from car_lectures_lesson32 import electrocar
#
# e_car = electrocar.ElectroCar('Tesla', 'T', 2018, 99_000)
# e_car.show_car()
# e_car.description_battery()

# 2 Вариант (упрощенный) - делает имя обращения короче

# from car_lectures_lesson32.electrocar import ElectroCar
#
# e_car = ElectroCar('Tesla', 'T', 2018, 99_000)
# e_car.show_car()
# e_car.description_battery()
# ---------------------------------------------------------------------------


# Задача
#
class PayrollSystem:
    def calculate(self, employees):
        print("Расчет заработной платы:")
        print('=' * 50)
        for employee in employees:
            print(f"Заработная плата: {employee.id_name} - {employee.name}")
            print(f"- Проверить сумму: {employee.calculate_payroll()}")
            print()


class Employee:
    def __init__(self, id_name, name):
        self.id_name = id_name
        self.name = name


class SalaryEmployee(Employee):
    """Административные работники, с фиксированной зарплатой"""
    def __init__(self, id_name, name, weekly_salary):
        super().__init__(id_name, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    """Сотрудники с почасовой зарплатой"""
    def __init__(self, id_name, name, hours_worked, hour_rate):
        super().__init__(id_name, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class SalesRepresentative(SalaryEmployee):
    def __init__(self, id_name, name, weekly_salary, commission_salary):
        super().__init__(id_name, name, weekly_salary)
        self.commission_salary = commission_salary

    def calculate_payroll(self):
        return self.weekly_salary + self.commission_salary


salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
sales_representative = SalesRepresentative(3, "Николай Хорольский", 1000,
                                           250)

payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    sales_representative
])
