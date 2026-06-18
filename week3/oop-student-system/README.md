# OOP Student Management System

## Project Overview

This project is a simple **Object-Oriented Programming (OOP) Student Management System** built using Python. It is a Week 3 internship task for practicing classes, objects, methods, attributes, `__init__`, and `self`.

In Week 2, I worked with student records using dictionaries and functions. In this project, I rebuilt the same student management idea using OOP so the program is more organized and easier to understand.

The system allows the user to:

* Add a student
* View all students
* Search for a student using Student ID
* Delete a student
* Handle invalid input without crashing
* Exit the program safely

---

## Project Folder Structure

```text
week3/oop-student-system/
├── student.py
├── management.py
├── main.py
├── README.md
└── screenshots/
```

---

## Files Used

### `student.py`

This file contains the `Student` class.

The `Student` class is used to store details of one student, including:

* Student ID
* Name
* University
* Major

It also has a `display()` method to print the student details in a clean format.

---

### `management.py`

This file contains the `StudentManager` class.

The `StudentManager` class manages all student records. It includes methods to:

* Add a new student
* View all students
* Search for a student
* Delete a student

It also includes input validation and `try / except` handling to avoid program crashes.

---

### `main.py`

This file contains the main menu and program loop.

It creates an object of the `StudentManager` class and uses that object to call the required methods based on the user's menu choice.

---

## OOP Concepts Used

This project uses the following OOP concepts:

### Class

A class is like a blueprint. In this project, the `Student` class is used as a blueprint for creating student objects.

### Object

An object is created from a class. Each student added to the system becomes a separate `Student` object.

### `__init__`

The `__init__` method runs automatically when a new object is created. It is used to store the starting values of the object.

### `self`

`self` refers to the current object. It helps the program store and access the correct data for each student.

### Attributes

Attributes are the data stored inside an object. In this project, examples of attributes are `student_id`, `name`, `university`, and `major`.

### Methods

Methods are actions that belong to a class. In this project, examples of methods are `display()`, `add_student()`, `view_all()`, `search()`, and `delete()`.

---

## How to Run the Program

1. Open the project folder in VS Code.
2. Make sure all three Python files are in the same folder:

   * `student.py`
   * `management.py`
   * `main.py`
3. Run the `main.py` file.

Command:

```bash
python main.py
```

---

## Menu Options

When the program runs, the user will see this menu:

```text
===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Delete Student
5. Exit
```

The user can enter a number from 1 to 5 to perform the required action.

---

## Testing

The program was tested using seven test cases.

| Test Case | Description                         |
| --------- | ----------------------------------- |
| Test 1    | Added a student successfully        |
| Test 2    | Viewed all student records          |
| Test 3    | Searched for an existing student    |
| Test 4    | Searched for a non-existing student |
| Test 5    | Deleted a student successfully      |
| Test 6    | Checked invalid input handling      |
| Test 7    | Exited the program safely           |

Screenshots of all test cases are stored inside the `screenshots` folder.

---

## Screenshots

The screenshots folder includes:

```text
test-1-add-student.png
test-2-view-all-students.png
test-3-search-existing-student.png
test-4-search-non-existing-student.png
test-5-delete-student.png
test-6-invalid-input.png
test-7-exit-program.png
```

---

## What I Learned

Through this project, I understood how OOP makes a program more structured. Instead of passing dictionaries between many separate functions, I learned how to group related data and actions together using classes.

The `Student` class represents one student, while the `StudentManager` class manages all student records. This made the program easier to read, update, and expand.

I also practiced using `try / except` again so that invalid input does not crash the program. This helped me connect my previous error handling task with the new OOP topic.

---

## GitHub Workflow

For this project, I followed a professional GitHub workflow by creating the Week 3 project folder, adding source code files, testing the program, saving screenshots, updating the README file, and preparing meaningful commits.

Example commit messages:

```text
add Student class
add StudentManager methods
add main menu loop
add input validation and testing
add README and screenshots
```

---

## Repository

Main Repository:

```text
https://github.com/haameedfouzaan007-alt/sohail-smart-solutions-internship
```

Project Folder:

```text
week3/oop-student-system/
```
