
from management import StudentManager



def main():
    # Create an object of StudentManager
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                print("\n--- Add Student ---")
                student_id = input("Student ID: ").strip()
                name = input("Name: ").strip()
                university = input("University: ").strip()
                major = input("Major: ").strip()

                manager.add_student(student_id, name, university, major)
                

            elif choice == 2:
                print("\n--- Student List ---")
                manager.view_all()

            elif choice == 3:
                print("\n--- Search Student ---")
                student_id = input("Enter Student ID: ").strip()

                student = manager.search(student_id)

                if student:
                    print("\nStudent Found:")
                    student.display()
                else:
                    print("No student found with that ID.")

            elif choice == 4:
                print("\n--- Delete Student ---")
                student_id = input("Enter Student ID: ").strip()
                manager.delete(student_id)

            elif choice == 5:
                print("Thank you for using the system. Goodbye!")
                break

            else:
                print("Please choose a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as error:
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
