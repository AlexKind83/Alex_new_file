from Homework.Task_38.movie_catalog.decorator import add_title


class UserInterface:
    @add_title(' Редактирование данных каталога фильмов ')
    def wait_user_answer(self):
        print('Действие с фильмами')
        print('1 - добавление фильма'
              '\n2 - каталог фильмов'
              '\n3 - просмотр определенного фильма'
              '\n4 - удаление фильма'
              '\nq - выход из программы')
        user_answer = input('Выбор вариантов действия: ')
        return user_answer

    @add_title('Запись данных о фильме')
    def add_user_catalog(self):
        """(1) Получаем данные от пользователя,
        и по ключу присваиваем значение, которое получаем от пользователя"""
        dict_catalog = {'название фильма': None,
                        'жанр': None,
                        'режиссер': None,
                        'год выпуска': None,
                        'длительность': None,
                        'студия': None,
                        'актеры': None,
                        }
        for key in dict_catalog:
            dict_catalog[key] = input(f'Введите {key}: ')
        return dict_catalog

    @add_title('Список фильмов')
    def look_all_catalogs(self, catalogs):
        """(2) Приходят значения. \n
         С enumerate(catalogs, start=1,) перебираем значения, начиная с числа 1."""
        for intel, catalog in enumerate(catalogs, start=1,):
            print(f'{intel}. {catalog}')

    @add_title('Ввод названия фильма')
    def get_user_movie(self):
        """(3) Вводим ключ который, хотим найти.
        В роли ключа выступают пользовательское значения которое попало в 'название фильма'.
        Внимание: {'name_film(зп)': {'name_film': зп, 'genre': зп, ...}} что находится в модуле model"""
        user_movie = input('Введите названия фильма: ')
        return user_movie

    @add_title('Просмотр фильма')
    def look_single_movie(self, catalog):
        """(3/2) Сюда уже приходят 'русский названия ключей'.
           Проходимся по названиям ключей key, и значениям ключей catalog[key]."""
        for key in catalog:
            print(f'{key} {catalog[key]}')

    @add_title('Сообщение об ошибке')
    def look_incorrect_name_film_error(self, user_film):
        print(f'Фильм с названием {user_film} не существует ')

    @add_title('Удаление фильма')
    def remove_single_movie(self, user_film):
        print(f'Фильм {user_film} был удален')

    @add_title('Сообщение об ошибке')
    def show_incorrect_catalog_error(self, answer):
        print(f'Вариант {answer} не существует')
