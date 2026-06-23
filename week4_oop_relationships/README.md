# Week 4 — OOP Relationships and JSON Persistence

## Project Overview

This project was completed as part of Week 4 of my internship at Sohail Smart Solutions.

The project started with object-oriented programming relationships, where I extended my previous Student Management System into a two-class design using `Student` and `Course`. After that, I improved the same project by adding file persistence using JSON, so the program can save data and load it again later.

This helped me understand two important ideas:

* How multiple classes can work together in a real program
* How program data can be saved permanently using JSON files

---

## Tasks Covered

### Task 1 — OOP Level 2: Relationships Between Objects

The first task focused on object relationships in Python. I used a `Student` class to represent one student and a `Course` class to manage multiple student objects.

### Task 2 — Making Data Last: File Persistence with JSON

The second task focused on saving and loading data. I added JSON persistence so the course and student data can be saved into a file and restored when the program runs again.

---

## Files Used

* `student.py` — contains the `Student` class
* `course.py` — contains the `Course` class and JSON save/load methods
* `main.py` — creates data, saves it, loads it back, and prints the output
* `course_data.json` — stores the saved course and student data
* `README.md` — explains the project, learning, and implementation
* `screenshots/` — contains output and JSON proof screenshots

---

# Task 1 — OOP Level 2: Relationships Between Objects

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

### Two-Class Design

In this project, I used two classes:

### Student Class

The `Student` class represents one student.

Each student stores:

* Student ID
* Student Name
* Grade

It also includes a `display()` method to show student details.

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

### Relationship Between the Classes

This project uses composition.

The `Course` class contains a list of `Student` objects. Instead of storing student information as plain text or dictionaries, the course stores actual student objects.

Example:

```python
course.add_student(student1)
```

This means the course is connected to student objects. The course can manage students, while each student still remains its own object.

---

# Task 2 — Making Data Last: File Persistence with JSON

## Part 1 — Learn

### Why Programs Need to Save State

Programs need to save state because data stored only in memory is temporary. While a Python program is running, variables and objects exist in memory. Once the program closes, that data is lost.

For example, if I create student objects during program execution and then close the program, those students will no longer exist unless the data has been saved externally. This is called in-memory data.

Persistent data means the data is saved outside the program, usually in a file or database. This allows the program to load the data again later. Real applications need this because users expect their information to still be available after closing and reopening the program.

### What JSON Is and Why It Is Used

JSON stands for JavaScript Object Notation. It is a lightweight format used for storing and exchanging data.

JSON is widely used because it is easy for both humans and programs to read. APIs, configuration files, datasets, and web applications often use JSON. It stores data using key-value pairs, which is very similar to Python dictionaries.

Example:

```json
{
    "name": "Haameed",
    "grade": 85
}
```

This structure is simple, readable, and easy to work with.

### Reading and Writing Files in Python

Python can read and write files using the `open()` function.

To write data to a file, we use `"w"` mode. To read data from a file, we use `"r"` mode.

It is better to use `with open()` because it automatically closes the file after the work is done. This is called a context manager.

Example:

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

Using `with` makes file handling cleaner and safer.

### The JSON Module

Python has a built-in `json` module that helps work with JSON files.

The `json.dump()` function is used to write Python data into a JSON file.

The `json.load()` function is used to read JSON data from a file and bring it back into Python.

In this project, I used `json.dump()` to save course and student data into `course_data.json`. I used `json.load()` to read the saved data back into the program.

### Turning Objects Into Saveable Data and Back

Python objects cannot be saved directly into JSON in a simple way. So first, the object needs to be converted into a dictionary.

In this project, I used a `to_dict()` method to convert objects into dictionary format. For the `Student` class, I connected this to the `__dict__` idea because `__dict__` stores the object attributes as a dictionary.

Example:

```python
def to_dict(self):
    return self.__dict__
```

To rebuild the object later, I used a `from_dict()` method. This method takes the saved dictionary and creates a new `Student` object from it.

This helped me understand how object data can be saved into a JSON file and restored later.

---

## Part 2 — Apply

### How My Data Is Saved and Restored

In this updated version of the project, I added file persistence using JSON.

Before adding JSON, the program only stored data while it was running. Once the program closed, the course and student details were lost. To solve this, I added two methods:

* `save_to_file(filename)`
* `load_from_file(filename)`

The `save_to_file()` method converts the course and student objects into dictionary format and saves them into a JSON file called `course_data.json`.

The `load_from_file()` method reads the JSON file and rebuilds the `Course` object and the `Student` objects from the saved data.

I also used `try/except` while reading and writing files. This helps the program handle errors properly, such as when the file does not exist or when the JSON file has invalid data.

---

## Program Workflow

The program follows this flow:

1. Create a course.
2. Create three student objects.
3. Add the students to the course.
4. Display the original course data.
5. Save the data into `course_data.json`.
6. Simulate closing and restarting the program.
7. Load the data back from the JSON file.
8. Display the loaded data to confirm everything is restored.

---

## Concepts Practiced

Through this project, I practiced:

* Classes and objects
* Composition
* Object relationships
* Instance attributes
* Lists of objects
* File handling
* Context managers
* JSON saving and loading
* `json.dump()`
* `json.load()`
* `to_dict()`
* `from_dict()`
* `__dict__`
* Error handling with `try/except`

---

## How to Run the Program

Open the project folder and run:

```bash
python main.py
```

---

## Sample Output

```text
Original Course Data
--------------------
Course Name: Python OOP Level 2

Students Enrolled:
ID: S001, Name: Haameed, Grade: 85
ID: S002, Name: Ahmed, Grade: 78
ID: S003, Name: Sara, Grade: 92

Average Grade: 85.0

Data saved successfully to course_data.json

Simulating program close and restart
------------------------------------

Data loaded successfully from course_data.json

Loaded Course Data
------------------
Course Name: Python OOP Level 2

Students Enrolled:
ID: S001, Name: Haameed, Grade: 85
ID: S002, Name: Ahmed, Grade: 78
ID: S003, Name: Sara, Grade: 92

Average Grade: 85.0
```

---

## JSON File Example

The saved data is stored in `course_data.json`.

Example:

```json
{
    "course_name": "Python OOP Level 2",
    "students": [
        {
            "student_id": "S001",
            "name": "Haameed",
            "grade": 85
        },
        {
            "student_id": "S002",
            "name": "Ahmed",
            "grade": 78
        },
        {
            "student_id": "S003",
            "name": "Sara",
            "grade": 92
        }
    ]
}
```

---

## Screenshots

The `screenshots` folder contains evidence of:

* OOP relationship output
* JSON save and load output
* `course_data.json` file proof

---

## Reflection

This Week 4 project helped me understand that object-oriented programming is not only about creating classes, but also about connecting classes together and managing data properly.

In Task 1, I learned how the `Course` class can contain multiple `Student` objects. This made the program more organized because each class had its own role. The `Student` class handled individual student information, while the `Course` class managed a group of students.

In Task 2, I learned why saving data is important. Before using JSON, the program forgot everything after it closed. After adding `save_to_file()` and `load_from_file()`, the program was able to save the course data and restore it again.

Overall, this project improved my understanding of object relationships, JSON file handling, and how real programs keep data after they close.
