# OOP Level 2 — Relationships Between Objects

## Part 1 — Learn

### Composition

Composition means one class contains objects from another class. In this project, the `Course` class contains many `Student` objects. This means the course is not only storing simple names or text. It is storing full student objects, where each student has their own student ID, name, and grade.

For example, one course can have three student objects inside it. The course can then add students, remove students, list students, and calculate the average grade. This shows how two classes can work together in an object-oriented program.

### Composition vs a Plain List of Dictionaries

A plain list of dictionaries can also store student data, but it is not as organized as using classes. A dictionary can store values like student ID, name, and grade, but the data and the behavior are not properly connected.

With composition, the `Student` class is responsible for student details, and the `Course` class is responsible for managing students. This makes the code easier to read, understand, and maintain. It also makes the program closer to how real software systems are structured.

### Class Attributes vs Instance Attributes

Class attributes are shared by all objects of a class. Instance attributes are different for each object.

For example, if all students belong to the same university, that could be a class attribute because it is common for all students. But student ID, name, and grade should be instance attributes because each student has different values.

In this project, `student_id`, `name`, and `grade` are instance attributes because every student object has its own information.

### Inheritance

Inheritance means one class can reuse the features of another class. The original class is called the parent class, and the new class is called the child class.

Example:

```python
class Person:
    def speak(self):
        print("This person can speak.")

class Student(Person):
    pass

student = Student()
student.speak()
```

In this example, the `Student` class inherits from the `Person` class. This means the student object can use the `speak()` method without writing it again inside the `Student` class.

### Why Grouping Related Classes Makes Code Easier to Extend

Grouping related classes makes code more organized and easier to improve later. Instead of writing everything inside one large class or one large file, each class can focus on one job.

In this project, the `Student` class stores individual student details, while the `Course` class manages a group of students. This makes the program easier to extend in the future. For example, attendance, assignments, course marks, or student reports can be added later without rewriting the full program.

This helped me understand that real software is usually made from multiple classes working together, not only one class.

---

## Part 2 — Apply

## Project Overview

This project was completed as part of Week 4 of my internship at Sohail Smart Solutions.

The goal of this task was to extend my previous Student Management System into a two-class design. In the previous OOP task, I worked with a single `Student` class. In this task, I added a `Course` class that manages multiple `Student` objects.

This project helped me understand object relationships and how classes can work together in a Python program.

---

## Files Used

* `student.py` — contains the `Student` class
* `course.py` — contains the `Course` class
* `main.py` — creates the course, adds students, and prints the summary
* `README.md` — explains the project and the relationship between the classes
* `screenshot/output.png` — shows the program output

---

## Classes Used

### Student Class

The `Student` class represents one student.

Each student stores:

* Student ID
* Student Name
* Grade

The class also includes a method to display student information.

### Course Class

The `Course` class represents a course that contains multiple students.

The class stores:

* Course Name
* List of Student Objects

The following methods were implemented:

* `add_student()`
* `remove_student()`
* `list_students()`
* `average_grade()`

---

## Relationship Between the Classes

This project uses composition.

The `Course` class contains a list of `Student` objects. Instead of storing student information as plain text or dictionaries, the course stores actual student objects.

Example:

```python
course.add_student(student1)
```

This means the course is connected to student objects. The course can manage students, while each student still remains its own object.

---

## Program Workflow

The program performs the following steps:

1. Creates a course.
2. Creates three student objects.
3. Adds the students to the course.
4. Displays all enrolled students.
5. Calculates and displays the average grade.

---

## Concepts Practiced

Through this project, I practiced:

* Classes and objects
* Composition
* Object relationships
* Instance attributes
* Methods
* Lists of objects
* Average grade calculation
* Basic object-oriented programming design

---

## How to Run the Program

Open the project folder and run:

```bash
python main.py
```

---

## Reflection

This task helped me understand that object-oriented programming is not only about creating classes, but also about connecting classes together.

Before this task, I mostly focused on creating one class and making it work. In this project, I learned how one class can contain and manage objects from another class. This made the program more organized and easier to understand.

The `Student` class handles individual student information, while the `Course` class manages a collection of students and performs operations on them.

Overall, this task improved my understanding of object relationships and gave me more confidence in working with object-oriented designs.
