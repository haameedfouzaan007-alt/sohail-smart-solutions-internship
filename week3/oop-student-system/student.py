class Student:
    """
    A simple class used to store and manage information about a student.
    Each student has an ID, name, university, and major.
    """

    def __init__(self, student_id, name, university, major):
        """
        Create a new student object and save the provided details.
        """
        self.student_id = student_id
        self.name = name
        self.university = university
        self.major = major

    def display(self):
        """
        Print the student's information in a clear and readable format.
        """
        print("\n----- Student Details -----")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("University :", self.university)
        print("Major      :", self.major)
