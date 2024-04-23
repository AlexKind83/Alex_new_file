"""Импортируем модули и классы, (model и view)"""
from Homework.Task_38.movie_catalog.view import UserInterface
from Homework.Task_38.movie_catalog.model import MovieCatalogModel


class Controller:
    """В этом классе будут происходить обмен данных между модулями view и model"""
    def __init__(self):
        """Инициализируем классы из модуля model, view"""
        self.movie_catalog_model = MovieCatalogModel()
        self.user_interface = UserInterface()

    def run(self):
        """Метод который, будет вызываться в модуле project_movie_catalog. \n
           Содержит цикл while с флагом для завершения. \n
           Также получает данные из модуля view, метода wait_user_answer. \n
           И передаем данные в этом классе в метод check_user_answer"""
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            catalog = self.user_interface.add_user_catalog()  # Получаем данные из view
            self.movie_catalog_model.add_catalog(catalog)  # Передаются данные в model
        elif answer == '2':
            catalogs = self.movie_catalog_model.get_all_catalogs()
            self.user_interface.look_all_catalogs(catalogs)
        elif answer == '3':
            watch_movie = self.user_interface.get_user_movie()
            try:
                movie = self.movie_catalog_model.get_single_movie(watch_movie)
            except KeyError:
                self.user_interface.look_incorrect_name_film_error(watch_movie)
            else:
                self.user_interface.look_single_movie(movie)
        elif answer == '4':
            catalog_name_film = self.user_interface.get_user_movie()
            try:
                catalog = self.movie_catalog_model.remove_name_film(catalog_name_film)
            except KeyError:
                self.user_interface.look_incorrect_name_film_error(catalog_name_film)
            else:
                self.user_interface.remove_single_movie(catalog)
        elif answer == 'q':
            pass
        else:
            self.user_interface.show_incorrect_catalog_error(answer)

