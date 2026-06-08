# Student Management System
# This program allows the user to add, view, search, and delete student records.

# List to store all student records
students = []


# Function to add a new student
def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    university = input("Enter University: ")
    major = input("Enter Major: ")

    # Input validation
    if student_id == "" or name == "" or university == "" or major == "":
        print("All fields are required. Student was not added.")
        return

    student = {
        "id": student_id,
        "name": name,
        "university": university,
        "major": major
    }

    students.append(student)
    print("Student added successfully!")


# Function to view all students
def view_students():
    print("\n--- View All Students ---")

    if len(students) == 0:
        print("No student records available.")
    else:
        for student in students:
            print("-------------------------")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("University:", student["university"])
            print("Major:", student["major"])


# Function to search for a student using Student ID
def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter Student ID to search: ")

    if search_id == "":
        print("Student ID cannot be empty.")
        return

    found = False

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found:")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("University:", student["university"])
            print("Major:", student["major"])
            found = True
            break

    if found == False:
        print("Student not found.")


# Function to delete a student using Student ID
def delete_student():
    print("\n--- Delete Student ---")

    delete_id = input("Enter Student ID to delete: ")

    if delete_id == "":
        print("Student ID cannot be empty.")
        return

    found = False

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            found = True
            break

    if found == False:
        print("Student not found. Cannot delete.")


# Function to display menu
def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


# Main program loop
while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
