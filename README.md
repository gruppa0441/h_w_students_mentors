# Текст кода по Домашнему заданию

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
        if isinstance(lecturer, Lecturer) and  course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grades(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        return round(sum_rating / len_rating, 2)    
      
    def __lt__(self, other):
        st_1 = self._average_grades()
        st_2 = other._average_grades()
        if st_1 > st_2:
          print(f'Лучший на курсе {self}')
        else:
          print(f'Лучший на курсе {other}')
        return 
  
    def __str__(self):
        return f'Студент:\n Имя:{self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self._average_grades()}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n Завершенные курсы: {", ".join(self.finished_courses)}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
              
    def _average_grades(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating,  2)
        return average_rating
      
    def __lt__(self, other):
        res = self._average_grades() < other._average_grades()
        if res == False:
          print(f'Лучший лектор: {self}')
        else:
          return print(f'Лучший лектор: {other}')
  
    def __str__(self):
        return f'Лектор:\n Имя:{self.name}\n Фамилия: {self.surname}\n Средняя оценка за ведение лекции: {self._average_grades()}'
         

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
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Bill', 'Bill')
lecturer_2.courses_attached += ['Git']

# Оценки
reviewer_1.rate_hw(student_1,'Python', 10)
reviewer_1.rate_hw(student_2,'Python', 7)
reviewer_2.rate_hw(student_1,'Git', 9)
reviewer_2.rate_hw(student_2,'Git', 5)

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Git', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Git', 9)

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