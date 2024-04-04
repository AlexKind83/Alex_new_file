"""Записать начало распаковки (тут рассказывают о старом)
   pickle - работает только с python
   Чтобы список мог работать в json мы его должны поместить в список"""

import pickle
import json

# Урок 33

"""Упаковка данных (сериализация, десериализация) """

# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоко', 'манго'],
#     'овощи': ['морковь'],
#     'Бюджет': 1000
# }
#
# with open(file_name, 'wb') as fn:
#     pickle.dump(shop_list, fn)
#
# with open(file_name, 'rb') as fn:
#     shop_list_2 = pickle.load(fn)
#
# print(shop_list_2)


#
#
# class Test:
#     num = 35
#     str = 'привет'
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f"число: {Test.num}\nСтрока: {Test.str}\nСписок: {Test.lst}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# print(obj)
# print()
#
# obj1 = pickle.dumps(obj)
# print(f"Сериализация в строке: \n{obj1}")
# print()
#
# obj2 = pickle.loads(obj1)
# print(f"Десериализация из строки: \n{obj2}")


# # Пропущена
# #
# class Tast2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Tast2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


""" Json """

# data = {
#     'name': 'Olga',
#     'age': 35,
#     20: None,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'first_name': 'Alice',
#             True: 1
#         }
#     ]
# }
#
# file_name = 'data_file.json'
#
# with open(file_name, 'w', encoding='UTF-8') as fw:
#     json.dump(data, fw)
#
# with open(file_name, 'r', encoding='UTF-8') as fw:
#     data1 = json.load(fw)
#
# print(data1)

# -------------------------------------------------------------

# Сохраняем в строку.
# Чтобы работать со строкой в json, нужно сначала ее считать.

# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,  # (1)
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'first_name': 'Alice',
#             'True': 1  # (1)
#         }
#     ]
# }
#
# json_string = json.dumps(data, sort_keys=True)  # (1) sort_keys=True
# # (сортировка ключей = все ключи должны быть строкой)
# print(json_string)
# print(type(json_string))
#
# data1 = json.loads(json_string)  # Считываем строку
# print(data1)
# print(type(data1))
#
#
# # Проблемы, которые возникают при, использование другого языка
# #
# x = {
#     'name': 'Виктор'
# }
# print(json.dumps(x))
# print(json.loads(json.dumps(x)))  # 1 способ чтобы кодировка не билась
# print(json.dumps(x, ensure_ascii=False))  # 2 способ чтобы кодировка не билась


# Чтобы список мог работать в json мы его должны поместить в список

from random import choice

def gen_person():
    name = ''
    tel = ''

    latter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(latter)
    # print(name)

    while len(tel) != 10:
        tel += choice(num)
    # print(tel)

    person = {
        'name': name,
        'tel': tel,
    }
    return person


# # 1 создаем список json
# person = []  # Помещаем в список
# for i in range(3):
#     person.append(gen_person())
#
# print(person)
#
# with open('person.json', 'w', encoding='UTF-8') as f:
#     json.dump(person, f, indent=2)


# 2 с помощью try/except создаем возможность не перезаписывать, а добавлять новые данные
# def write_json(person_dict):
#     try:  # Помогает не перезаписывать, а прибавлять
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('person.json', 'w', encoding='UTF-8') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(1):
#     write_json(gen_person())



# Задача
#
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ', '.join(map(str, self.marks))  # Записать (распаковка без скобок, в один ряд)
        return f"Студент: {self.name}: {a}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 1)

    def dump_to_json(self):  # (2)
        data = {'name': self.name, 'marks': self.marks}
        with open(self.get_file_name(), 'w', encoding='UTF-8') as f:
            json.dump(data, f)

    def load_from_file(self):  # (2)
        with open(self.get_file_name(), 'r', encoding='UTF-8') as f:
            print(json.load(f))

    def get_file_name(self):
        return self.name + '.json'  # (2) записать (добавление любого студента)


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = '\n'.join(map(str, self.students))  # (1) Чтобы код выводился, надо преобразовать в строку
        return f"\nГруппа: {self.group} \n{a}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group_1, group_2, index):
        group_2.add_student(group_1.remove_student(index))  # переводим из группы в группу студента


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])

print(st1)
st1.add_mark(4)
# print(st1)
st1.delete_mark(2)
# print(st1)
st1.edit_mark(4, 5)
print(st1)
print(st1.average_mark())


sts1 = [st1, st2]
group1 = Group(sts1, "ГК Python")  # (1)
# print(group1)
group1.add_student(st3)
# print(group1)
group1.remove_student(1)
print(group1)

sts2 = [st2]
group2 = Group(sts2, "ГК Web")
print(group2)

Group.change_group(group1, group2, 0)  # тут 1 из какой, 2 в какой, по индексу студента
print(group1)
print(group2)

st1.dump_to_json()
st1.load_from_file()
