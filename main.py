class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        s_ = 0
        q_ = 0
        for course in self.grades.values():
            s_ += sum(course)
            q_ += len(course)
        return round(s_ / q_, 2)

    def __lt__(self, other):
        st_1 = self.average_grades()
        st_2 = other.average_grades()
        if st_1 > st_2:
            print(f'Лучший на курсе {self}')
        else:
            print(f'Лучший на курсе {other}')
        return

    def __str__(self):
        return f'Студент:\n Имя:{self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_grades()}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        s_ = 0
        q_ = 0
        for course in self.grades.values():
            s_ += sum(course)
            q_ += len(course)
        return round(s_ / q_, 2)

    def __lt__(self, other):
        res = self.average_grades() < other.average_grades()
        if res is False:
            print(f'Лучший лектор: {self}')
        else:
            return print(f'Лучший лектор: {other}')

    def __str__(self):
        return f'Лектор:\n Имя:{self.name}\n Фамилия: {self.surname}\n Средняя оценка за ведение лекции: {self.average_grades()}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Проверяющий ДЗ студнтов:\n Имя:{self.name}\n Фамилия: {self.surname}'


# Студенты
student_1 = Student('Jon', 'Jon', 'M')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2 = Student('Jen', 'Jen', 'W')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Git']

# Проверяющие ДЗ студентв
reviewer_1 = Reviewer('Tom', 'Tom')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Jerry', 'Jerry')
reviewer_2.courses_attached += ['Git']

# Лекторы
lecturer_1 = Lecturer('Bob', 'Bob')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Bill', 'Bill')
lecturer_2.courses_attached += ['Python', 'Git']

# Оценки
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)

student_1.rate_lecturer(lecturer_2, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Python', 7)

student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 7)

student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

# Средняя оценка на курсе
students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]


def average_rating_students_for_course(course, students_list):
    s_ = 0
    q_ = 0
    for student in students_list:
        for course in student.grades:
            stud_sum_rating = student.average_grades()
            s_ += stud_sum_rating
            q_ += 1
    average_rating = round(s_ / q_, 2)
    return f'Cредняя оценка студентов курса {course} - {average_rating}'


def average_rating_lecturers_for_course(course, lecturers_list):
    s_ = 0
    q_ = 0
    for lecturer in lecturers_list:
        for course in lecturer.grades:
            stud_sum_rating = lecturer.average_grades()
            s_ += stud_sum_rating
            q_ += 1
    average_rating = round(s_ / q_, 2)
    return f'Cредняя оценка лекторов курса {course} - {average_rating}'


# Вывод данных
print(reviewer_1)
print(reviewer_2)
print()
print(lecturer_1)
print(lecturer_2)
print()
print(student_1)
print(student_2)
print()
print(student_1.__lt__(student_2))
print(lecturer_1.__lt__(lecturer_2))
print()
print(average_rating_students_for_course('Python', students_list))
print(average_rating_lecturers_for_course('Python', lecturers_list))

