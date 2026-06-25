import json
import csv
from student import Student


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        if not self.students:
            print("No students available in this course.")
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

    @classmethod
    def from_dict(cls, data):
        course = cls(data["course_name"])

        for student_data in data["students"]:
            student = Student.from_dict(student_data)
            course.add_student(student)

        return course


def save_courses_to_file(courses, filename):
    try:
        data = [course.to_dict() for course in courses]

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Data saved successfully to {filename}")

    except OSError:
        print("Error: Could not save data to the file.")


def load_courses_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        courses = []

        for course_data in data:
            course = Course.from_dict(course_data)
            courses.append(course)

        print(f"Data loaded successfully from {filename}")
        return courses

    except FileNotFoundError:
        print("Error: File not found.")
        return []

    except json.JSONDecodeError:
        print("Error: JSON file is not valid.")
        return []

    except KeyError:
        print("Error: Some required data is missing.")
        return []

    except OSError:
        print("Error: Could not read the file.")
        return []


def export_courses_to_csv(courses, filename):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["student_id", "name", "course", "grade"])

            for course in courses:
                for student in course.students:
                    writer.writerow([
                        student.student_id,
                        student.name,
                        course.course_name,
                        student.grade
                    ])

        print(f"Data exported successfully to {filename}")

    except OSError:
        print("Error: Could not export data to CSV.")