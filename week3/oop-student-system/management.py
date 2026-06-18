
from student import Student


class StudentManager:
    """
    Handles all student records and provides methods
    to add, view, search, and delete students.
    """

    def __init__(self):
        # Store students using student_id as the key
        self.students = {}

    def add_student(self, student_id, name, university, major):
        """Add a new student to the system."""
        try:
            student_id = student_id.strip()
            name = name.strip()
            university = university.strip()
            major = major.strip()

            # Make sure no field is left empty
            if not student_id or not name or not university or not major:
                print("Error: All fields are required. Student was not added.")
                return

            # Prevent duplicate student IDs
            if student_id in self.students:
                print("Error: A student with this ID already exists.")
                return

            student = Student(student_id, name, university, major)
            self.students[student_id] = student

            print("Student added successfully.")

        except Exception as error:
            print("Something went wrong while adding the student.")
            print("Error:", error)

    def view_all(self):
        """Display all saved student records."""
        try:
            if not self.students:
                print("No student records found.")
                return

            print("\n===== All Student Records =====")
            for student in self.students.values():
                student.display()

        except Exception as error:
            print("Something went wrong while viewing students.")
            print("Error:", error)

    def search(self, student_id):
        """Find and return a student by ID."""
        try:
            student_id = student_id.strip()

            if not student_id:
                print("Error: Student ID cannot be empty.")
                return None

            return self.students.get(student_id)

        except Exception as error:
            print("Something went wrong while searching for the student.")
            print("Error:", error)
            return None

    def delete(self, student_id):
        """Remove a student record using the student ID."""
        try:
            student_id = student_id.strip()

            if not student_id:
                print("Error: Student ID cannot be empty.")
                return

            if student_id in self.students:
                del self.students[student_id]
                print("Student deleted successfully.")
            else:
                print("Student not found. Cannot delete.")

        except Exception as error:
            print("Something went wrong while deleting the student.")
            print("Error:", error)
