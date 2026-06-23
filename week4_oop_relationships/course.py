class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def list_students(self):
        if not self.students:
            print("No students enrolled in this course.")
        else:
            for student in self.students:
                print(student.display())

    def average_grade(self):
        if not self.students:
            return 0

        total = 0
        for student in self.students:
            total += student.grade

        return total / len(self.students)