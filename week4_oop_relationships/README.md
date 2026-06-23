# OOP Level 2 — Relationships Between Objects

## Project Overview

This project was completed as part of Week 4 of my internship at Sohail Smart Solutions.

The goal of this task was to understand how multiple classes can work together in an object-oriented program. In the previous OOP task, I worked with a single `Student` class. In this task, I extended the design by introducing a `Course` class that manages multiple student objects.

This helped me understand how real software systems are organized using relationships between classes instead of putting everything into one class.

---

## Classes Used

### Student Class

The `Student` class represents a single student.

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

This project uses **composition**.

The `Course` class contains a list of `Student` objects. Instead of storing student information as plain text or dictionaries, the course stores actual student objects.

For example:

```python
course.add_student(student1)
```

This creates a relationship where the course manages multiple students while each student remains its own object.

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

* Classes and Objects
* Composition
* Object Relationships
* Instance Attributes
* Methods
* Lists of Objects
* Basic Data Processing
* Object-Oriented Programming Principles

---

## How to Run the Program

Open the project folder and run:

```bash
python main.py
```

---

## Reflection

This task helped me understand that object-oriented programming is not only about creating classes but also about connecting classes together.

Previously, I focused on creating a single class and making it work correctly. In this project, I learned how one class can contain and manage objects from another class. This made the program more organized and easier to extend.

I found the idea of composition useful because it reflects how real systems are structured. The `Student` class handles individual student information, while the `Course` class manages a collection of students and performs operations on them.

Overall, this task improved my understanding of object relationships and gave me more confidence in working with object-oriented designs.
