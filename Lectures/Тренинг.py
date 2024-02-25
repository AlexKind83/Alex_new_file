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


