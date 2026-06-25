# Week 4 — Structured Student Analytics Tool

## Project Overview

This mini-project was completed as part of Week 4 of my internship at Sohail Smart Solutions.

The purpose of this project is to combine the main concepts I learned during the internship into one small tool. This project uses object-oriented programming, JSON file saving and loading, error handling, CSV export, and pandas analysis.

The tool manages student records using classes, saves the data into a JSON file, exports the data into a CSV file, and then uses pandas to produce simple analytics.

---

## Part 1 — Learn

### What Makes a Project Clean

A clean project is easy to understand and easy to maintain. The files should be organized properly, and each file should have a clear purpose.

In this project, I separated the work into different files:

* `student.py` handles student details.
* `course.py` handles courses, JSON saving/loading, and CSV export.
* `analytics.py` handles pandas analysis.
* `main.py` runs the full program.

This makes the project easier to read instead of putting everything into one large file.

### Why a Good README Matters

A README file is important because it is usually the first thing someone reads on GitHub.

A good README explains what the project does, what files are included, how to run the program, and what concepts were practiced. It helps others understand the project without needing to guess from the code only.

### Simple Program Flow

The program follows a simple flow:

```text
Input → Process → Output
```

For this project:

* Input: student records
* Process: save data, load data, export CSV, analyze using pandas
* Output: JSON file, CSV file, and analytics results

This flow helped me understand how a small real program works from start to end.

### Separation of Concerns

Separation of concerns means each part of the program has its own job.

In this project, the OOP code manages the student and course records. The JSON part saves and loads the data, and the pandas part analyzes the data.

This makes the project cleaner and easier to understand.

---

## Part 2 — Apply

## Files Included

* `student.py` — contains the `Student` class
* `course.py` — contains the `Course` class and file handling functions
* `analytics.py` — contains pandas analysis code
* `main.py` — runs the full project
* `students_data.json` — stores saved student data
* `students.csv` — exported CSV file used for analysis
* `README.md` — explains the project
* `screenshots/` — contains output screenshots

---

## Features

This tool can:

* Create student records using OOP classes
* Store students inside course objects
* Save course and student data into a JSON file
* Load data back from the JSON file
* Export data into a CSV file
* Analyze student data using pandas
* Show useful insights from the data

---

## Analytics Produced

The pandas analysis gives these insights:

1. Average grade per course
2. Top student with the highest grade
3. Number of students per course
4. Students who scored above 80

---

## How to Run the Program

Open the project folder and run:

```bash
python main.py
```

If pandas is not installed, install it using:

```bash
pip install pandas
```

Then run the program again.

---

## Sample Output

```text
Original Student Records
------------------------

Course: Python OOP
ID: S001, Name: Haameed, Grade: 85
ID: S002, Name: Ahmed, Grade: 78
Average Grade: 81.5

Course: Data Handling
ID: S003, Name: Sara, Grade: 92
ID: S004, Name: Mariam, Grade: 88
Average Grade: 90.0

Course: AI Basics
ID: S005, Name: Omar, Grade: 74
Average Grade: 74.0

Saving data...
Data saved successfully to students_data.json

Loading data back...
Data loaded successfully from students_data.json

Exporting data to CSV...
Data exported successfully to students.csv

Running pandas analysis...

Student Analytics Results
-------------------------
```

---

## What I Learned

This project helped me understand how different programming concepts can work together in one small tool.

I learned how OOP can be used to organize records using classes. I also learned how JSON can save data permanently so the program does not lose everything after closing. After that, I used pandas to analyze the saved data and produce useful results.

This task also helped me understand why clean project structure and README documentation are important. A project becomes easier to understand when the files are separated properly and each part has its own responsibility.
