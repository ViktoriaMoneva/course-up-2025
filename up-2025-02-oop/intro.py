class Student:
    def __init__(self, name, fn, semester):
        self.name = name
        self.semester = semester
        self.fn = fn
    def change_semester(self, new_semester):
        self.semester = new_semester
    def __str__(self):
        return f'Student({self.name}, {self.fn}, {self.semester})'

if __name__ == '__main__':
    pass