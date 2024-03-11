# import time
# stat = time.time()
#
# # # Проверка пин кода из 4 или 6 цифр, и не должно быть букв
# #
# # import re
# #
# # # def validate_pin(pin):
# # #     if len(pin) == 4 and pin.isdigit() or len(pin) == 6 and pin.isdigit():
# # #         return True
# # #     else:
# # #         return False
# #
# # # 2
# # # def validate_pin(pin):
# # #     return len(pin) in (4, 6) and pin.isdigit()
# #
# # # 3
# # def validate_pin(pin):
# #     # return true or false
# #     return bool(re.fullmatch(r"\d{4}|\d{6}", pin))
# #
# #
# # validate_pin('1234')
# # validate_pin('12t4')
# # validate_pin('12345')
# # validate_pin('1234f')
# # validate_pin('123456')
# # validate_pin('1234r6')
#
#
# # Поиск единственного уникального числа
#
# # def find_uniq(arr):
# #     for n in arr:
# #         if arr.count(n) == 1:
# #             return n
# #
# #
# # def find_uniq(arr):
# #     x, y = sorted(arr).count(arr), sorted(arr)[-1]
# #     print(x, y)
# #
# #
# # def find_uniq(arr):
# #     for n in set(arr):
# #         if arr.count(n) == 1:
# #             return n
# #
# #
# # print(find_uniq([1, 1, 1, 2, 1, 1]))
# # print(find_uniq([0, 0, 0.55, 0, 0]))
# # print(find_uniq([10, 3, 3, 3, 3]))
#
# import re
#
# # Отделить цифры от строки и вывести как число
#
# # регулярным выражением
# # def filter_string(st):
# #     n = re.sub(r'\D+', '', st)
# #     return int(n)
#
#
# # # Через фильтр Самый удачный
# # def filter_string(st):
# #     return int(''.join(filter(str.isdigit, st)))
#
#
# # Через цикл
# # def filter_string(string):
# #     return int(''.join(n for n in string if n.isdigit()))
#
#
# # # Через lambda
# # filter_string = lambda string: int(''.join([i for i in string if i.isdigit()]))
#
#
# # print(filter_string("aa1bb2cc3dd"))
# # print(filter_string("11bb2c23c3"))
#
#
# end = time.time()
# print(end - stat)
import math
# class Box:
#     def __init__(self, cat = None):
#         self.cat = cat
#         self.nextcat = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def contains(self, cat):
#         """Проверяет есть или нет узлы в списке"""
#         lastbox = self.head
#         while (lastbox):
#             if cat == lastbox.cat:
#                 return True
#             else:
#                 lastbox = lastbox.nextcat
#         return False
#
#     def addToEnd(self, newcat):
#         """Добавить элементы в список. \n
#            Добавляем узел в конец списка """
#         newbox = Box(newcat)
#         if self.head is None:
#             self.head = newbox
#             return
#         lastbox = self.head
#         while lastbox.nextcat:
#             lastbox = lastbox.nextcat
#         lastbox.nextcat = newbox
#
#     def get(self, catIndex):
#         """"""
#         lastbox = self.head
#         boxIndex = 0
#         while boxIndex <= catIndex:
#             if boxIndex == catIndex:
#                 return lastbox.cat
#             boxIndex = boxIndex + 1
#             lastbox = lastbox.nextcat
#
#
# l1 = LinkedList()
# l1.addToEnd('one')
# l1.addToEnd('two')
# l1.addToEnd('three')
#
# print(l1.contains('one'))
#
# print(l1.get(2))
