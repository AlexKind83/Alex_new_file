from parser_homework_37 import Parser


def parser_start_homework_37():
    for i in range(1, 5):
        pars = Parser(f'https://python-teach.ru/category/python-dlya-nachinayushhih/stroki-v-python/page/{i}/',
                      'file_homework_37.txt')
        pars.run()


if __name__ == '__main__':
    parser_start_homework_37()
