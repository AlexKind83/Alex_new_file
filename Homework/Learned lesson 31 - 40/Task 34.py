import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ', '.join(map(str, self.marks))
        return f"Студент: {self.name}: {a}"

    def add_mark(self, mark):
        """Добавляем оценку студенту"""
        self.marks.append(mark)

    def delete_mark(self, index):
        """Удаление оценки студента"""
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        """Заменяем оценку на другую, у студента"""
        self.marks[index] = new_mark

    def average_mark(self):
        """Средний бал всех оценок студента"""
        return round(sum(self.marks) / len(self.marks), 1)

    def dump_to_json(self):
        """Создаем файл по имени студента"""
        data = {'name': self.name, 'marks': self.marks}
        with open(self.get_file_name(), 'w', encoding='UTF-8') as f:
            json.dump(data, f)

    def load_from_file(self):
        """Открываем файл по мени студента"""
        with open(self.get_file_name(), 'r', encoding='UTF-8') as f:
            print(json.load(f))

    def get_file_name(self):
        """Вспомогательный метод для создания и открытия файлов"""
        return self.name + '.json'


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = '\n'.join(map(str, self.students))
        return f"\nГруппа: {self.group} \n{a}"

    def add_student(self, student):
        """Добавляем студента в группу"""
        self.students.append(student)

    def remove_student(self, index):
        """Удаляем студента из группы"""
        return self.students.pop(index)

    @staticmethod
    def change_group(group_1, group_2, index):
        """Перемещаем студента из одной группы в другую"""
        group_2.add_student(group_1.remove_student(index))

    def get_student(self):
        """Распаковка - распаковываем данные о студенте"""
        return [{'name': student.name, 'marks': student.marks} for student in self.students]

    def dump_to_json(self):
        """Записываем группы, и находящий в них студентов в файл json"""
        a_data = {self.group: self.get_student()}

        try:
            data = json.load(open(self.get_file_name()))
        except FileNotFoundError:
            data = []

        data.append(a_data)
        with open(self.get_file_name(), 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=2)

    def get_file_name(self):
        """Вспомогательный метод - содержит имя файла"""
        return 'groups' + '.json'

    def load_from_file(self):
        """Загружает данные из json"""
        with open(self.get_file_name(), 'r', encoding="UTF-8") as f:
            print(json.load(f))


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])

gr1 = [st1]
gr2 = [st2]
gr3 = [st3]

group1 = Group(gr1, 'Web')
group2 = Group(gr2, 'Python')
group3 = Group(gr3, 'JavaScript')

group1.dump_to_json()
group2.dump_to_json()
group3.dump_to_json()

group1.load_from_file()
