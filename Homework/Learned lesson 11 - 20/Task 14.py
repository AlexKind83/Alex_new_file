students_number = int(input('Количество студентов: '))
students = []
estimation = []

for i in range(students_number):
    i += 1
    s = input(str(i) + '-й студент: ')
    e = int(input('Балл: '))
    students.append(s)
    estimation.append(e)
estimation_sum = sum(estimation)
estimation_average = round(estimation_sum / students_number)

print()
print("Средний балл: ", estimation_average, '. ', "Студенты с баллом выше среднего:", sep='')

students_dict = {students: estimation for students, estimation in zip(students, estimation)}

for i in students:
    if students_dict[i] >= estimation_average:
        print(i)
