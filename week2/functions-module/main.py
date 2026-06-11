# Main program to test student_utils module

import student_utils


# Sample student data
students = {
    "Haameed": "AURAK",
    "Ali": "University of Sharjah",
    "Sara": "AURAK"
}


print("===== Functions and Modules Task =====")

# Test 1: Student exists
print("\nTest 1: Search Existing Student")
result = student_utils.find_student(students, "Haameed")
print("Haameed studies at:", result)

# Test 2: Student does not exist
print("\nTest 2: Search Non-Existing Student")
result = student_utils.find_student(students, "Omar")

if result is None:
    print("Student not found.")
else:
    print("Omar studies at:", result)

# Test 3: Add new student
print("\nTest 3: Add New Student")
students = student_utils.add_student(students, "Mariam", "Khalifa University")
print("Updated Student Records:", students)

# Test 4: Display unique universities
print("\nTest 4: Unique Universities")
universities = student_utils.unique_universities(students)
print("Unique Universities:", universities)

