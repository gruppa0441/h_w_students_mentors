class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

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

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self._average_rating = 0

    def _average_rating(self, lecturer, course, grade):
        res = sum(int([grade['course'] for course, grade in self.grades])) / len(self.grades)
        return res

    def __str__(self):
        res = f'Lecturer:\n Имя:{self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {Lecturer._average_rating}'
        return res

student_1 = Student('Jim', 'Jim', 'M')
student_2 = Student('Jon', 'Jon', 'M')
student_3 = Student('Jen', 'Jen', 'W')

student_1.courses_in_progress += ['Pithon']
student_2.courses_in_progress += ['Pithon']
student_3.courses_in_progress += ['Pithon']

