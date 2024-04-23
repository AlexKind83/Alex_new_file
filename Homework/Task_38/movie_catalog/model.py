class MovieCatalog:
    def __init__(self, name_film, genre, director, year_release, duration_film, studio, actors):
        """Инициализируем приходящий аргументы. \n"""
        self.name_film = name_film
        self.genre = genre
        self.director = director
        self.year_release = year_release
        self.duration_film = duration_film
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.name_film} ({self.year_release}г. {self.genre})'


class MovieCatalogModel:
    """Получаем список словарей, где стартовым ключом будет значение пользователя,
    которое приходит в name_film"""
    def __init__(self):
        self.catalogs = {}  # {'name_film(зп)': {'name_film': зп, 'genre': зп, ...}}

    def add_catalog(self, dict_catalog):
        """(1) [catalog = MovieCatalog(*dict_catalog.values())]
        Получаем только значения, и они записываются как аргументы, args помогает распечатать список. \n
        [self.catalogs[catalog.name_film] = catalog]
        Приходят по ключу name_film: ключ из параметров MovieCatalog, и значение которое ввел пользователь.
        Это не обходимая мера чтобы не перезаписались ключи."""
        catalog = MovieCatalog(*dict_catalog.values())  # MovieCatalog(значение пользователя, зп, зп, ...)
        self.catalogs[catalog.name_film] = catalog  # {'name_film(зп)': {'name_film': зп, 'genre': зп, ...}}

    def get_all_catalogs(self):
        """(2) Возвращаем значения из (self.catalogs = {})"""
        return self.catalogs.values()

    def get_single_movie(self, name_film):
        """(3) catalog = self.catalogs[name_film] Запрашиваем данные по ключу.
        catalog.name_film Возвращаются значения по (name_film, genre, ...).
         Возвращаем Ключи 'русские'. """
        catalog = self.catalogs[name_film]
        dict_catalog = {'название фильма': catalog.name_film,
                        'жанр': catalog.genre,
                        'режиссер': catalog.director,
                        'год выпуска': catalog.year_release,
                        'длительность': catalog.duration_film,
                        'студия': catalog.studio,
                        'актеры': catalog.actors,
                        }
        return dict_catalog

    def remove_name_film(self, name_film):
        return self.catalogs.pop(name_film)
