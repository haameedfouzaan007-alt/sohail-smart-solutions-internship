class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"], data["name"], data["grade"])