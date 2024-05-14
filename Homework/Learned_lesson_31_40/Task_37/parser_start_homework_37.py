from parser_homework_37 import Parser


def parser_start_homework_37():
    """Содержит адрес, и файл для сохранения.
       Содержит цикл для возможности обработке данных с не скольки https страниц.
       Принимает метод-класса для вызова, из модуля parser_homework"""
    for i in range(1, 5):
        pars = Parser(f'https://python-teach.ru/category/python-dlya-nachinayushhih/stroki-v-python/page/{i}/',
                      'file_homework_37.txt')
        pars.run()


if __name__ == '__main__':
    parser_start_homework_37()
