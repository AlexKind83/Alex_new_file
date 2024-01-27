# Тут много способов вывести эти номера

import re

phone_list = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
reg = r'[\s\d\D]*'
print(re.search(reg, phone_list).group())
print()


def phone_list(tel):
    reg_ = r'.*'
    return re.search(reg_, tel).group()


print(phone_list('+7 499 456-45-78'))
print(phone_list('+74994564578'))
print(phone_list('7 (499) 456 45 78'))
print(phone_list('7 (499) 456-45-78'))