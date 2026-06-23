import json
from student import Student


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

    def to_dict(self):
        return {
            "course_name": self.course_name,
            "students": [student.to_dict() for student in self.students]
        }

    def save_to_file(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, indent=4)

            print(f"\nData saved successfully to {filename}")

        except OSError:
            print("\nError: Could not save data to the file.")

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            course = cls(data["course_name"])

            for student_data in data["students"]:
                student = Student.from_dict(student_data)
                course.add_student(student)

            print(f"\nData loaded successfully from {filename}")
            return course

        except FileNotFoundError:
            print("\nError: File not found. Returning an empty course.")
            return cls("Empty Course")

        except json.JSONDecodeError:
            print("\nError: The file is not valid JSON. Returning an empty course.")
            return cls("Empty Course")

        except KeyError:
            print("\nError: Some required data is missing in the JSON file.")
            return cls("Empty Course")

        except OSError:
            print("\nError: Could not read the file.")
            return cls("Empty Course")