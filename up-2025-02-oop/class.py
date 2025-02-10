all_students = []

class Student:
    next_id = 0
    @staticmethod
    def get_next_id():
    def __init__(self, name, fn, semester):
        Student.next_id += 1
        self.id = Student.next_id
        self.name = name
        self.semester = semester
        self.fn = fn
    def change_semester(self, new_semester):
        self.semester = new_semester
    def __repr__(self):
        return f'Student(Name: {self.name}, FN:{self.fn}, Sem: {self.semester})'

if __name__ == '__main__':
    trayan = Student('Trayan Iliev', '0MI12345', 2)
    print(trayan)
    print(trayan.fn)
    trayan.change_semester(3)
    print(f'{id(trayan)}: {trayan}')

    george = Student('George','OPH23235', 1)
    print(f'{id(george)}: {george}')

    all_students.append(trayan)
    all_students.append(george)

    print(all_students)

