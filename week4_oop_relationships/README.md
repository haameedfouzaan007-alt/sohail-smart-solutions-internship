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


## Task 2 — Making Data Last: File Persistence with JSON

### Part 1 — Learn

### Why Programs Need to Save State

Programs need to save state because data stored only in memory is temporary. While a Python program is running, variables and objects exist in memory. However, once the program is closed, all that data is lost.

For example, if I create student objects during program execution and then close the program, those students will no longer exist unless the data has been saved externally. This type of data is known as in-memory data.

Persistent data, on the other hand, is stored outside the program, typically in a file or database. This allows the program to reload the data when it is run again. In real-world applications, persistence is essential because users expect their data to remain available even after closing and reopening the application.

### What JSON Is and Why It Is Used

JSON stands for JavaScript Object Notation. It is a lightweight and widely used format for storing and exchanging data.

JSON is popular because it is easy for both humans and machines to read and understand. It is commonly used in APIs, configuration files, datasets, and web applications. JSON represents data using key-value pairs, which closely resemble Python dictionaries.

Example:

```json
{
    "name": "Haameed",
    "grade": 85
}
```

This structure is simple, readable, and easy to work with.

### Reading and Writing Files in Python

Python provides built-in support for reading and writing files using the `open()` function.

To write data to a file, we use `"w"` mode, and to read data, we use `"r"` mode.

It is considered best practice to use the `with open()` statement, as it automatically handles closing the file after the operation is complete. This approach is known as using a context manager.

Example:

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

Using `with` ensures that file handling is both safe and efficient.

### The JSON Module

Python includes a built-in `json` module that simplifies working with JSON data.

The `json.dump()` function is used to write Python data structures to a JSON file.

The `json.load()` function is used to read data from a JSON file and convert it back into Python objects.

In this project, I used `json.dump()` to store course and student data in a file named `course_data.json`, and `json.load()` to retrieve and reconstruct that data.

### Converting Objects to Saveable Data and Back

Python objects cannot be directly stored in JSON format. Therefore, they must first be converted into a dictionary representation.

In this project, I implemented a `to_dict()` method to convert objects into dictionaries. For the `Student` class, this was simplified by using the `__dict__` attribute, which automatically stores an object's attributes as a dictionary.

Example:

```python
def to_dict(self):
    return self.__dict__
```

To recreate objects from saved data, I implemented a `from_dict()` method. This method takes a dictionary and uses it to construct a new `Student` object.

This approach allowed me to effectively save object data to a JSON file and restore it when needed.

---

## Part 2 — Apply

### How My Data Is Saved and Restored

In this updated version of the project, I implemented file persistence using JSON.

Previously, the program stored data only during runtime. Once the program was closed, all course and student information was lost. To address this, I added two methods: `save_to_file()` and `load_from_file()`.

The `save_to_file()` method converts course and student objects into dictionary format and saves them to a JSON file named `course_data.json`.

The `load_from_file()` method reads the JSON file and reconstructs the `Course` and `Student` objects from the stored data.

Additionally, I used `try/except` blocks when reading from and writing to files. This ensures that the program can handle potential errors gracefully, such as missing files or invalid JSON data.

This task helped me clearly understand the difference between temporary in-memory data and persistent data stored in external files.
