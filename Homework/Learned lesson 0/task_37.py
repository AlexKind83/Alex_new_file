from Task_37_parser import Parser


def task_37():
    for i in range(1, 13):
        pars = Parser(f'https://python-teach.ru/category/python-dlya-nachinayushhih/page/{i}/',
                  'text.txt')
        pars.run()


if __name__ == '__main__':
    task_37()
