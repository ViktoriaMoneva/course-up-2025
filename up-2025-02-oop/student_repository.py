from intro import Student


class StudentRepository:
    def __init__(self, students=None):
        self.students = students if students is not None else []
    def add_student(self, student):
        self.students.append(student)
    def get_all_students(self):
        return self.students




if __name__ == '__main__':
    course1_repo = StudentRepository()
    course2_repo = StudentRepository()
    george = Student('George','OPH23235', 1)
    course1_repo.students.append(george)
    print(course1_repo.students)
    print(course2_repo.students)
