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
        # print(res)

    def __str__(self):
        res = f'Lecturer:\n Имя:{self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {Lecturer._average_rating}'
        return res


class Reviewer(Mentor):
    pass

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        print(student.grades)

    def __str__(self):
        res = f'Reviewer:\n Имя:{self.name}\n Фамилия: {self.surname}'
        return res


best_Student = Student('Ruoy', 'Eman', 'your_gender')
best_Student.courses_in_progress += ['Python']

cool_Lecturer = Lecturer('Arni', 'Shvarch')
cool_Lecturer.courses_attached += ['Python']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']

best_Student.rate_lecturer(cool_Lecturer, 'Python', 10)
best_Student.rate_lecturer(cool_Lecturer, 'Python', 10)
best_Student.rate_lecturer(cool_Lecturer, 'Python', 10)

cool_Reviewer.rate_hw(best_Student, 'Python', 10)
cool_Reviewer.rate_hw(best_Student, 'Python', 10)
cool_Reviewer.rate_hw(best_Student, 'Python', 10)

# print(f'оценки лучшему студенту: {best_Student.grades}')
# print(f'оценки лучшему лектору: {cool_Lecturer.grades}')


print(cool_Reviewer)
print(cool_Lecturer)
