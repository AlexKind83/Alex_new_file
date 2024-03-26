# (1)
# from car_lectures_lesson32 import carclass


# class ElectroCar(carclass.CarClass):
#     def __init__(self, brand, model, year, probeg):
#         super().__init__(brand, model, year, probeg)
#         self.battery = 100
#
#     def description_battery(self):
#         print(f"Этот автомобиль имеет мощность {self.battery}%")


# (2)
from car_lectures_lesson32.carclass import CarClass


class ElectroCar(CarClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = 100

    def description_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery}%")
