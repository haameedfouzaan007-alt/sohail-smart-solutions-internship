from student import Student
from course import Course

course = Course("Python OOP Level 2")

student1 = Student("S001", "Haameed", 85)
student2 = Student("S002", "Ahmed", 78)
student3 = Student("S003", "Sara", 92)

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

print("Course Summary")
print("--------------")
print("Course Name:", course.course_name)

print("\nStudents Enrolled:")
course.list_students()

print("\nAverage Grade:", course.average_grade())