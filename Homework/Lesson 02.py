month = int(input('Введите номер месяца: '))
if 1 <= month <= 2 or month == 12:
    print('Зима')
elif 3 <= month <= 5:
    print('Весна')
elif 6 <= month <= 8:
    print('Лето')
elif 9 <= month <= 11:
    print('Осень')
else:
    print('Ошибка ввода данных')


# month = int(input('Введите номер месяца: '))
# if (month >= 1) and (month <= 2) or (month == 12):
#     if month == 12:
#         print('Декабрь, зима')
#     if month == 1:
#         print('Январь, зима')
#     if month == 2:
#         print('Февраль, зима')
# elif (month >= 3) and (month <= 5):
#     if month == 3:
#         print('Март, весна')
#     if month == 4:
#         print('Апрель, весна')
#     if month == 5:
#         print('Май, весна')
# elif (month >= 6) and (month <= 8):
#     if month == 6:
#         print('Июнь, лето')
#     if month == 7:
#         print('Июль, лето')
#     if month == 8:
#         print('Август, лето')
# elif (month >= 9) and (month <= 11):
#     if month == 9:
#         print('Сентябрь, осень')
#     if month == 10:
#         print('Октябрь, осень')
#     if month == 11:
#         print('Ноябрь, осень')
# else:
#     print('Такого месяца не существует')
