from student import Student
from course import Course


filename = "course_data.json"

# Create course
course = Course("Python OOP Level 2")

# Create students
student1 = Student("S001", "Haameed", 85)
student2 = Student("S002", "Ahmed", 78)
student3 = Student("S003", "Sara", 92)

# Add students to course
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

print("Original Course Data")
print("--------------------")
print("Course Name:", course.course_name)

print("\nStudents Enrolled:")
course.list_students()

print("\nAverage Grade:", course.average_grade())

# Save data to JSON file
course.save_to_file(filename)

print("\nSimulating program close and restart")
print("------------------------------------")

# Load data back from JSON file
loaded_course = Course.load_from_file(filename)

print("\nLoaded Course Data")
print("------------------")
print("Course Name:", loaded_course.course_name)

print("\nStudents Enrolled:")
loaded_course.list_students()

print("\nAverage Grade:", loaded_course.average_grade())