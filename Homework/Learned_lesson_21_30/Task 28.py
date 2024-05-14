class Student:
    def __init__(self, name):
        self._name = name
        self.make = self.Laptop().make()
        self.model = self.Laptop().model()
        self.op = self.Laptop().operational_memory()

    def __str__(self):
        return f"{self._name} => Ноутбук: {self.make} {self.model}, {self.op}"

    class Laptop:
        @staticmethod
        def make():
            return 'Intel'

        @staticmethod
        def model():
            return 'Core-i7'

        @staticmethod
        def operational_memory():
            return 'RAM 16 ГБ'


# student1 = Student('Andrei')
# print(student1)
# student2 = Student('Irina')
# print(student2)

students = (Student('Andrei'), Student('Irina'))

for student in students:
    print(student)
