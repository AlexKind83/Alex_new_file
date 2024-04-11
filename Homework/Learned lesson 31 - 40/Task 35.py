"""Выводим данные в консоль из файла data2.csv"""
import csv

with open('data2.csv', encoding='UTF-8') as f:
    file_datas = csv.reader(f, delimiter=';')
    count = 0
    for file_data in file_datas:
        if count == 0:  # обязательное условие если хотим разделить текс вывода
            print(f"Файл содержит столбцы: {', '.join(file_data)}")
        else:
            print(f" Имя доменна: {file_data[0]}, Поставщик: {file_data[1]}, "
                  f"Номер: {file_data[2]}, Локация: {file_data[3]}")
        count += 1
