class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average(self):
        temp_value = 0
        count_value = 0
        for key, value in self.grades.items():
            for elem in value:
                temp_value += elem
                count_value += 1

        if count_value != 0:
            average_rating = round((temp_value / count_value), 1)
            return float(average_rating)
        else:
            return 'Студент не имеет оценок!'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average()}\n' \
               f'Курсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}\n' \
               f'Завершенные курсы: {", ".join(map(str, self.finished_courses))}'

    def estimate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other):
        # Определяет поведение оператора равенства, ==.
        if not isinstance(other, Student):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, ' \
                   f'т.к. {other.name} {other.surname} не является студентом!'

        if self.average() == other.average():
            return f'{self.name} {self.surname} и {other.name} {other.surname} имеют одинаковый средний балл ' \
                   f'за домашние задания - {self.average()}'
        else:
            return f'Средние баллы за домашние задания у {self.name} {self.surname} ({self.average()}) и ' \
                   f'{other.name} {other.surname} ({other.average()}) не равны!'

    def __ne__(self, other):
        # Определяет поведение оператора неравенства, !=.
        if not isinstance(other, Student):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, т.к. ' \
                   f'{other.name} {other.surname} не является студентом!'

        if self.average() != other.average():
            return f'Средние баллы за домашние задания у {self.name} {self.surname} ({self.average()}) и ' \
                   f'{other.name} {other.surname} ({other.average()}) не равны!'
        else:
            return f'Утверждение, что средние баллы за домашние задания у ' \
                   f'{self.name} {self.surname} ({self.average()}) и ' \
                   f'{other.name} {other.surname} ({other.average()}) не равны - ЛОЖНОЕ'

    def __lt__(self, other):
        # Определяет поведение оператора меньше, <.
        if not isinstance(other, Student):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, ' \
                   f'т.к. {other.name} {other.surname} не является студентом!'

        if self.average() < other.average():
            return f'Средний балл за домашние задания у {self.name} {self.surname} ({self.average()}) меньше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'
        else:
            return f'Средний балл за домашние задания у ' \
                   f'{self.name} {self.surname} ({self.average()}) НЕ меньше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'

    def __gt__(self, other):
        # Определяет поведение оператора больше, >.
        if not isinstance(other, Student):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, ' \
                   f'т.к. {other.name} {other.surname} не является студентом!'

        if self.average() > other.average():
            return f'Средний балл за домашние задания у {self.name} {self.surname} ({self.average()}) больше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'
        else:
            return f'Средний балл за домашние задания у ' \
                   f'{self.name} {self.surname} ({self.average()}) НЕ больше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Lecturer имеют возможность получать оценки за лекции от студентов по 10-балльной шкале."""

    grades = {}

    def average(self):
        temp_value = 0
        count_value = 0
        for key, value in self.grades.items():
            for elem in value:
                temp_value += elem
                count_value += 1

        if count_value != 0:
            average_rating = round((temp_value / count_value), 1)
            return float(average_rating)
        else:
            return 'Лектор не имеет оценок!'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'

    # Задание № 3. Полиморфизм и магические методы
    # 2. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции
    # и студентов по средней оценке за домашние задания.

    def __eq__(self, other):
        # Определяет поведение оператора равенства, ==.
        if not isinstance(other, Lecturer):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, ' \
                   f'т.к. {other.name} {other.surname} не является лектором!'

        if self.average() == other.average():
            return f'{self.name} {self.surname} и {other.name} {other.surname} имеют одинаковый средний балл ' \
                   f'за лекции - {self.average()}'
        else:
            return f'Средние баллы за лекции у {self.name} {self.surname} ({self.average()}) и ' \
                   f'{other.name} {other.surname} ({other.average()}) не равны!'

    def __ne__(self, other):
        # Определяет поведение оператора неравенства, !=.
        if not isinstance(other, Lecturer):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, т.к. ' \
                   f'{other.name} {other.surname} не является лектором!'

        if self.average() != other.average():
            return f'Средние баллы за лекции у {self.name} {self.surname} ({self.average()}) и ' \
                   f'{other.name} {other.surname} ({other.average()}) не равны!'
        else:
            return f'Утверждение, что средние баллы за лекции у {self.name} {self.surname} ({self.average()}) и ' \
                   f'{other.name} {other.surname} ({other.average()}) не равны - ЛОЖНОЕ'

    def __lt__(self, other):
        # Определяет поведение оператора меньше, <.
        if not isinstance(other, Lecturer):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, ' \
                   f'т.к. {other.name} {other.surname} не является лектором!'

        if self.average() < other.average():
            return f'Средний балл за лекции у {self.name} {self.surname} ({self.average()}) меньше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'
        else:
            return f'Средний балл за лекции у {self.name} {self.surname} ({self.average()}) НЕ меньше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'

    def __gt__(self, other):
        # Определяет поведение оператора больше, >.
        if not isinstance(other, Lecturer):
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}, ' \
                   f'т.к. {other.name} {other.surname} не является лектором!'

        if self.average() > other.average():
            return f'Средний балл за лекции у {self.name} {self.surname} ({self.average()}) больше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'
        else:
            return f'Средний балл за лекции у {self.name} {self.surname} ({self.average()}) НЕ больше чем у ' \
                   f'{other.name} {other.surname} ({other.average()})'


class Reviewer(Mentor):
    """Reviewer имеют возможность выставлять студентам оценки за домашние задания."""

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (course in self.courses_attached or course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(f'Ревьювер {cool_mentor.name} {cool_mentor.surname} оценил студента {best_student.name} {best_student.surname}:\n'
      f'{best_student.grades}')
print('###')

cool_lecturer = Lecturer('John', 'Star')
cool_lecturer.courses_attached += ['Python']

best_student.estimate(cool_lecturer, 'Python', 10)
best_student.estimate(cool_lecturer, 'Python', 9)
best_student.estimate(cool_lecturer, 'Python', 6)

print(f'Студент {best_student.name} {best_student.surname} оценил работу '
      f'лектора {cool_lecturer.name} {cool_lecturer.surname}:\n{cool_lecturer.grades}')
print('###')
print(cool_mentor)
print('###')
print(cool_lecturer)
print('###')
print(best_student)
print('###')

best_student2 = Student('Antony', 'Oldman', 'male')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

cool_mentor.rate_hw(best_student2, 'Python', 7)
cool_mentor.rate_hw(best_student2, 'Git', 9)
cool_mentor.rate_hw(best_student2, 'Python', 10)

cool_lecturer2 = Lecturer('Jack', 'Sparrow')
cool_lecturer2.courses_attached += ['Git']

best_student.estimate(cool_lecturer2, 'Git', 9)
best_student.estimate(cool_lecturer2, 'Git', 10)
best_student.estimate(cool_lecturer2, 'Git', 7)


# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы

student_1 = Student('Rick', 'Osborn', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Введение в программирование']
student_1.finished_courses += ['Git']

student_2 = Student('Bob', 'Robinson', 'male')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Введение в программирование']
student_2.finished_courses += ['Python']

mentor_1 = Mentor('Rick', 'Martin')
mentor_1.courses_attached += ['Python']

mentor_2 = Mentor('Alice', 'Svang')
mentor_2.courses_attached += ['Git']

lecturer_1 = Lecturer('Will', 'Smith')
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Antony', 'Rockford')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Johnny', 'Depp')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Robert', 'String')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['Введение в программирование']

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_1, 'Git', 10)

student_1.estimate(lecturer_1, 'Python', 9)
student_1.estimate(lecturer_1, 'Git', 10)

student_2.estimate(lecturer_2, 'Python', 8)


def average_student_grade_per_course(course, list_students):
    temporary_list = []
    for student in list_students:
        if course in student.grades.keys():
            for grade in student.grades[course]:
                temporary_list.append(grade)

    if len(temporary_list) != 0:
        average_rating = f'Средний балл у студентов по курсу "{course}" ' \
                         f'составляет {round(sum(temporary_list) / len(temporary_list), 1)}'
        return average_rating
    else:
        return f'У указанных студентов нет оценок за курс "{course}"!'


print(average_student_grade_per_course('Python', [best_student, best_student2, student_1, student_2]))
print(average_student_grade_per_course('Git', [best_student, best_student2, student_1, student_2]))
print(average_student_grade_per_course('Введение в программирование',
                                       [best_student, best_student2, student_1, student_2]))
print('###')


def average_lecturer_grade_per_course(course, list_lecturers):
    temporary_list = []
    for lecturer in list_lecturers:
        if course in lecturer.grades.keys():
            for grade in lecturer.grades[course]:
                temporary_list.append(grade)

    if len(temporary_list) != 0:
        average_rating = f'Средний балл у лекторов по курсу "{course}" ' \
                         f'составляет {round(sum(temporary_list) / len(temporary_list), 1)}'
        return average_rating
    else:
        return f'У указанных лекторов нет оценок за курс "{course}"!'


print(average_lecturer_grade_per_course('Python', [cool_lecturer, cool_lecturer2, lecturer_1, lecturer_2]))
print(average_lecturer_grade_per_course('Git', [cool_lecturer, cool_lecturer2, lecturer_1, lecturer_2]))
print(average_lecturer_grade_per_course('Введение в программирование',
                                        [cool_lecturer, cool_lecturer2, lecturer_1, lecturer_2]))
print('###')
print('СРАВНЕНИЕ')
print('<', cool_lecturer < cool_lecturer2)
print('>', cool_lecturer > cool_lecturer2)
print('==', cool_lecturer == cool_lecturer2)
print('!=', cool_lecturer != cool_lecturer2)
print('###')
print('<', best_student < best_student2)
print('>', best_student > best_student2)
print('==', best_student == best_student2)
print('!=', best_student != best_student2)
print('###')
print('<', cool_lecturer < best_student2)
print('>', best_student > cool_lecturer2)
print('==', cool_lecturer == best_student2)
print('!=', best_student != cool_lecturer2)
print('###')
