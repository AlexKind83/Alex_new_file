# Урок 22

# # Сохранить можно только строковое значение
# #
# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# # Задача  РАЗОБРАТСЯ ЗАПИСАТЬ
# #
# f = open('task_lesson_22_1.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменитьт строку в списке;\nзаписапь список в файл;\n")
# f.close()
#
# f = open('task_lesson_22_1.txt', 'r')
# rl = f.readlines()
# f.close()
#
# print(rl)
# rl[1] = "Hello World\n"
# print(rl)
# #
# #
# f = open('task_lesson_22_1.txt', 'w')
# f.writelines(rl)
# f.close()
#
# # Самостоятельное
# #
# filename = "task_lesson_22_1.txt"
# f = open(filename, "r")
# rl = f.readlines()
# f.close()
#
# print(rl)
#
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 <= pos < len(rl):
#     rl.pop(pos)
# else:
#     print("Индекс введен не верно")
#
# print(rl)
#
# f = open(filename, "w")
# f.writelines(rl)
# f.close()


# # Дополнительные методы
# #
# f = open('test2.txt', 'r')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # переместил курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test2.txt', 'w+')
# print(f.write("I am learning Python"))
# print(f.tell())
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# # В этой варианте файл закрывается когда мы выходим из with
# #
# with open('test2.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test2.txt', 'r') as f:
#     for line in f:
#         print(line[:3])


# # #  РАЗОБРАТЬСЯ ПОД ВИДЕО
# # #
# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
# with open(file_name, 'w') as f:
#     f.write(str(lst))  # сохранит список и числа, как строку
#
# print('Done!')
# #
# # 2
#
# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))  # 4.5 2.8 3.9 1.0 0.3 4.33 7.777
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list))
# print(len(nums_list))
#
# print('Done!')


# # Задача Разбирать
# #
# def longest_worlds(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))  # длинна самого длинного слова
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds('Worlds.txt'))


#
#
# one = 'one.txt'
# two = 'wto.txt'
#
# # text = ("Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\n"
# #         "Строка №8\nСтрока №9\nСтрока №10\n")
# #
# # with open(one, 'w', encoding='utf-8') as f:
# #     f.write(text)
#
# with open(one, 'r', encoding='utf-8') as fr, open(two, 'w', encoding='utf-8') as fw:
#     for line in fr:
#         line = line.replace("Строка", 'Линия -')
#         print(line)
#         fw.write(line)







# Урок 23

#  Модули OS и OS.PATH
#
import os
import time

# print(os.getcwd())  # путь к текущей директорий

# print(os.listdir())  # список директорий и файлов

# print(os.listdir(".."))  # выход на уровень выше

# os.mkdir("Созданная папка")  # создание папки

# os.makedirs("Папка1/Папка2/Папка3")  # создание папки с промежуточными директориями

# os.rmdir("Созданная папка")  # возможность удаления папки

# os.remove("xyz.txt")  # Удаление файла

# os.rename("Папка1", "Перейменованная папка")  # переименовать папку

# os.rename("Worlds.txt", "Перейменованная папка/words_new.txt")  # перейменовали файл и переместили в заданную
# # директорию

# os.renames("wto.txt", "folder/file.txt")  # переименовывали файл и переместили в заданную директорию,
# # при этом может создать промежуточные директорий


#


# os.mkdir('Test_folder')
# for i in range(1, 4):
#     with open(f'Test_folder/file{i}.txt', 'w') as file:
#         ...
# os.mkdir('Test_folder/Inner_test_folder1')
# for i in range(4, 9):
#     with open(f'Test_folder/Inner_test_folder1/file{i}.txt', 'w') as file:
#         ...
# os.mkdir('Test_folder/Inner_test_folder2')
# for i in range(9, 15):
#     with open(f'Test_folder/Inner_test_folder2/file{i}.txt', 'w') as file:
#         ...

# Посмотреть ВИДЕО ЗАПИСЬ УПУСТИЛ МЕТОД
#
# for root, dirs, files in os.walk('Work', topdown=False):
#     print('Root:', root)
#     print('Subdirs', dirs)
#     print('Files:', files)


#  ОПЯТЬ УПУСТИЛ ВС
#


# import os.path нужен для использования определенных методов которых нет в import os
#

# print(os.path.split(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures'))
# (print(os.path.split(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures')[0])
# print(os.path.split(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures')[1])
# print(os.path.dirname(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures'))  # [0]
# print(os.path.basename(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures'))  # [1])

# print(os.path.join(r'C:\Users\RobotComp.ru', 'Desktop', 'Новая папка', 'Python учеба', 'Lectures'))
# print(os.path.join('Новая папка', 'Python учеба', r'C:\Users\RobotComp.ru', 'Desktop', 'Lectures'))


# Задача ПЕРЕСМОТРЕТЬ ЧТО_ТО НЕ ТАК СДЕЛАЛ
#
# Создали нужные папки
# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
#
# # Создаем словарь где ключ это папки и файлы внутри папок
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f.11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# # Создаем файлы
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         # print(file_path)  # проверили что попадет в файл file_path
#         open(file_path, 'w').close()  # файл создали и сразу закрыли
#
# #
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Какой-то текс для файла расположенного по пути: {file}")
#
#
# #
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree('Work', False)
# print_tree('Work', True)


# # Проверяет существование пути (к папке или к файлу)
# print(os.path.exists(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures\Test_folder'))

# # Проверяет, что указанный путь является правильным путем к файлу
# print(os.path.isfile(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures\Test_folder'))

# # является правильный путь к папке
# print(os.path.isdir(r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures\Test_folder'))


#
#
# path = 'mein.py'
# print(os.path.getsize(path))  # возвращает размер файла в байтах (FileNotFoundError)
# print(os.path.getsize(path) // 1024)  # размер в килобайтах


# path = 'mein.py'
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу (в секундах)
# print(os.path.getctime(path))  # возвращает время создания файла
# print(os.path.getmtime(path))  # возвращает время последнего изменения файла
#
# print(time.strftime("%d.%m%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))


# # Задача
# #
# file_path = r'C:\Users\RobotComp.ru\Desktop\Новая папка\Python учеба\Lectures\Work\F2\F21\f212.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     print(f"{name} ({dirs}) - последний доступ к файлу: {os.path.getatime(file_path)}")
# else:
#     print(f"Файл {file_path} не существует")
