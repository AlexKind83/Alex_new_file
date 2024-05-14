""""""
import json

# Урок 34


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ', '.join(map(str, self.marks))  # Записать (распаковка без скобок, в один ряд)
#         return f"Студент: {self.name}: {a}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 1)
#
#     def dump_to_json(self):
#         data = {'name': self.name, 'marks': self.marks}
#         with open(self.get_file_name(), 'w', encoding='UTF-8') as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), 'r', encoding='UTF-8') as f:
#             print(json.load(f))
#
#     def get_file_name(self):
#         return self.name + '.json'
#
#
# class Group:
#     def __init__(self, students, group: str):
#         self.students = students
#         self.group: str = group
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))  # (1) Чтобы код выводился, надо преобразовать в строку
#         return f"\nГруппа: {self.group} \n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group_1, group_2, index):
#         group_2.add_student(group_1.remove_student(index))
#
#     def dump_to_json(self):
#         data = [
#                 {'name': student.name, 'marks': student.marks} for student in self.students
#         ]
#
#         with open(self.get_file_name(), 'w', encoding='UTF-8') as f:
#             json.dump(data, f, indent=2)
#
#     def get_file_name(self):
#         # self.group.lower().replace(' ', '-')
#         return self.group + '.json'
#
#     def load_from_file(self):
#         with open(self.get_file_name(), 'r', encoding="UTF-8") as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# # print(st1)
# st1.add_mark(4)
# # print(st1)
# st1.delete_mark(2)
# # print(st1)
# st1.edit_mark(4, 5)
# # print(st1)
# # print(st1.average_mark())
#
#
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК Python")  # (1)
# # print(group1)
# group1.add_student(st3)
# # print(group1)
# group1.remove_student(1)
# # print(group1)
#
# sts2 = [st2]
# group2 = Group(sts2, "ГК Web")
# # print(group2)
#
# Group.change_group(group1, group2, 0)
# # print(group1)
# # print(group2)
#
# group2.dump_to_json()
# group2.load_from_file()


# Задача
#


class CountryCapital:
    @staticmethod
    def add_country(file_name):
        new_country = input("Введите название страны: ")
        new_capital = input("Введите название столицы: ")

        try:  # Записать код
            data = json.load(open(file_name))
        except FileNotFoundError:
            data = {}

        data[new_country] = new_capital

        with open(file_name, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r', encoding='UTF-8') as f:

            print({k.cpitalize(): v.cpitalize() for k, v in json.load(f).items()})


file = "List_capital.json"

while True:
    index = input("Выбор действия:\n1 - Добавления данных\n2 - Удаление данных\n3 - Поиск данных"
                  "\n4 - Редактирование данных\n5 - Просмотр данных\n6 - Завершение работы\nВвод: ")
    if index == '1':
        CountryCapital.add_country(file)
    elif index == '5':
        CountryCapital.load_from_file(file)
    elif index == '6':
        break
    else:
        print("Введен некорректный номер")
