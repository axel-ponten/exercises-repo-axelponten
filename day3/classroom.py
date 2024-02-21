class Person():
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name  = last_name

    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name

class Student(Person):
    def __init__(self, first_name: str, last_name: str, subject_area: str) -> None:
        super().__init__(first_name, last_name)
        self.subject_area = subject_area

    def get_name_and_subject(self):
        return self.get_full_name() + " " + self.subject_area

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, course: str) -> None:
        super().__init__(first_name, last_name)
        self.course = course

    def get_name_and_course(self):
        return self.get_full_name() + " " + self.course
    