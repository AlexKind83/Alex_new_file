import re

# Самый лучший вариант в конкретном случай
text_2 = ("123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru,"
          "login.3-67@i.ru, 1login@ru.name.ru")
reg_2 = r'[\w.-]+@[\w.]+'
print(re.findall(reg_2, text_2))

print()

# Используем вместо "+" фигурные скобки (этот способ хорош когда нужно указать конкретную длину)
text_3 = ("123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru,"
          "login.3-67@i.ru, 1login@ru.name.ru")
reg_3 = r'[\w.-]{1,}@[\w.]{1,}'
print(re.findall(reg_3, text_3))

print()

# Самый длинный и плохой способ написания регулярного выражения
text_1 = ("123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru,"
          "login.3-67@i.ru, 1login@ru.name.ru")
reg_1 = r'[0-9a-zA-zА-я-.]+@[0-9a-zA-ZА-я.]+'
print(re.findall(reg_1, text_1))
