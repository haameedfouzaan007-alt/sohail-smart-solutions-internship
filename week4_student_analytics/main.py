from student import Student
from course import Course
from course import save_courses_to_file
from course import load_courses_from_file
from course import export_courses_to_csv
from analytics import run_analysis


json_filename = "students_data.json"
csv_filename = "students.csv"

# Create course objects
python_course = Course("Python OOP")
data_course = Course("Data Handling")
ai_course = Course("AI Basics")

# Add students to courses
python_course.add_student(Student("S001", "Haameed", 85))
python_course.add_student(Student("S002", "Ahmed", 78))

data_course.add_student(Student("S003", "Sara", 92))
data_course.add_student(Student("S004", "Mariam", 88))

ai_course.add_student(Student("S005", "Omar", 74))

courses = [python_course, data_course, ai_course]

print("Original Student Records")
print("------------------------")

for course in courses:
    print("\nCourse:", course.course_name)
    course.list_students()
    print("Average Grade:", course.average_grade())

print("\nSaving data...")
save_courses_to_file(courses, json_filename)

print("\nLoading data back...")
loaded_courses = load_courses_from_file(json_filename)

print("\nLoaded Student Records")
print("----------------------")

for course in loaded_courses:
    print("\nCourse:", course.course_name)
    course.list_students()

print("\nExporting data to CSV...")
export_courses_to_csv(loaded_courses, csv_filename)

print("\nRunning pandas analysis...")
run_analysis(csv_filename)