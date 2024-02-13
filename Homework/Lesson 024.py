class Car:

    def __init__(self, model, year_manufacture, manufacturer, engine_power, color, price):
        self.model = model
        self.year_manufacture = year_manufacture
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

        """ Этот способ применим до объявления в переменную """
#         print(" Данные автомобиля ".center(40, *'*'))
#         print("Название модели:", self.model, '\n'
#               "Год выпуска:", self.year_manufacture, '\n'
#               "Производитель:", self.manufacturer, '\n'
#               "Мощность двигателя:", self.engine_power, '\n'
#               "Цвет машины:", self.color, '\n'
#               "Цена:", self.price)
#         print('=' * 40)

    def print_info(self):
        """Этот метод многофункциональный \n
        1 - Можно инициализировать параметры до объявления в переменную \n
        2 - Есть возможность изменить параметры отдельными функциями \n"""
        print(" Данные автомобиля ".center(40, *'*'))
        print("Название модели:", self.model, '\n'
              "Год выпуска:", self.year_manufacture, '\n'
              "Производитель:", self.manufacturer, '\n'
              "Мощность двигателя:", self.engine_power, '\n'
              "Цвет машины:", self.color, '\n'
              "Цена:", self.price)
        print('=' * 40)

    def set_model(self, model):
        self.model = model

    def set_year(self, year_manufacture):
        self.year_manufacture = year_manufacture

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


# Car("X7 M50i", 2021, 'BMW', '530 л.с.', 'white', 10_790_000)
car1 = Car('', '', '', '', '', '')
car1.set_model('X7 M50i')
car1.set_year(2021)
car1.set_manufacturer('BMW')
car1.set_engine_power('530 л.с.')
car1.set_color('Белый')
car1.set_price(10_790_000)
car1.print_info()
