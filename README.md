# Sohail Smart Solutions Internship

This repository contains my internship tasks, source code, documentation, screenshots, notebooks, and project work completed during my internship with **Sohail Smart Solutions**.

The main purpose of this repository is to keep my internship work organized in one place and show my learning progress week by week. It also helps me practice using GitHub in a more professional way.

---

## Internship Details

* **Student Name:** Haameed Fouzaan Shake Hameedu
* **University:** American University of Ras Al Khaimah (AURAK)
* **Major:** Artificial Intelligence
* **Internship Site:** Sohail Smart Solutions
* **Internship Mode:** Remote / Online

---

## About This Repository

This repository includes my weekly internship tasks, programming practice, project files, README documentation, screenshots, Colab notebooks, and supporting materials.

Throughout the internship, I am using this repository to:

* Track my weekly progress
* Organize my code and documentation
* Practice Git and GitHub workflow
* Improve my programming and documentation skills
* Build small projects step by step
* Connect programming concepts with data and AI-related work

I am still learning and improving, so this repository also shows my progress from basic programming tasks to more structured Python and data-related projects.

---

## Tools and Technologies Used

* Python
* C++
* Git
* GitHub
* Visual Studio Code
* Google Colab
* Markdown
* JSON
* CSV
* pandas
* matplotlib

---

## Repository Structure

```text
sohail-smart-solutions-internship/
│
├── week1/
│   ├── Task-2-Binary-Search/
│   └── Task-4-Python-Grade-Calculator/
│
├── week2/
│   ├── student-management-system/
│   ├── functions-module/
│   └── error-handling/
│
├── week3/
│   └── oop-student-system/
│
├── week4_oop_relationships/
│   ├── student.py
│   ├── course.py
│   ├── main.py
│   ├── course_data.json
│   ├── README.md
│   └── screenshots/
│
├── week4_pandas_intro/
│   ├── week4_pandas_intro.ipynb
│   ├── students.csv
│   └── README.md
│
├── week4_student_analytics/
│   ├── student.py
│   ├── course.py
│   ├── analytics.py
│   ├── main.py
│   ├── students_data.json
│   ├── students.csv
│   ├── README.md
│   └── screenshots/
│
├── week5_data_cleaning/
│   ├── week5_data_cleaning.ipynb
│   ├── messy_students.csv
│   ├── cleaned_students.csv
│   └── README.md
│
├── week5_visualization/
│   ├── week5_visualization.ipynb
│   ├── cleaned_students.csv
│   └── README.md
│
├── README.md
└── .gitignore
```

---

## Weekly Work Summary

## Week 1 — Internship Onboarding and Programming Basics

In Week 1, I worked on internship onboarding, self-assessment, GitHub basics, and programming fundamentals.

### Main Work Completed

* Internship onboarding assessment
* Self-assessment and learning goals
* GitHub setup and workflow practice
* Binary Search task in C++
* Python Grade Calculator project
* README writing and documentation practice

### What I Learned

This week helped me understand the basic expectations of the internship. I also started practicing how to organize my work and upload tasks properly to GitHub.

---

## Week 2 — Python Fundamentals and Error Handling

In Week 2, I practiced Python fundamentals and worked on small projects to improve my coding confidence.

### Main Work Completed

* Student Management System
* Functions and modules practice
* Code reuse using separate files
* Error handling using `try` and `except`
* Input validation
* README documentation
* Testing screenshots

### What I Learned

This week helped me understand how to write cleaner Python code. I also learned how to handle user mistakes without crashing the program.

The error handling task was useful because it showed me why defensive programming is important in real applications.

---

## Week 3 — Object-Oriented Programming

In Week 3, I worked on object-oriented programming by rebuilding the Student Management System using classes and objects.

### Main Project

```text
week3/oop-student-system/
```

### Main Concepts Practiced

* Classes and objects
* `__init__`
* `self`
* Student class
* StudentManager class
* Menu-based program
* Input validation
* Error handling
* Documentation and screenshots

### What I Learned

This week helped me understand how programs can be organized using objects instead of only functions and dictionaries.

I also started understanding how classes can make a program easier to manage when the project becomes bigger.

---

## Week 4 — OOP Relationships, JSON, pandas, and Mini-Project

In Week 4, I continued with object-oriented programming and started moving toward data handling and analysis.

---

### Task 1: OOP Level 2 — Relationships Between Objects

### Folder

```text
week4_oop_relationships/
```

In this task, I extended the Student Management System into a two-class design using `Student` and `Course`.

The `Course` class stores multiple `Student` objects. This helped me understand composition and how different classes can work together in a program.

### Main Concepts Practiced

* Composition
* Multiple classes working together
* Lists of objects
* Class relationships
* Average grade calculation
* README documentation

---

### Task 2: Making Data Last — JSON Persistence

This task was added to the same Week 4 OOP project.

I updated the project so it can save course and student data into a JSON file and load it back again later.

### Main Concepts Practiced

* JSON files
* `json.dump()`
* `json.load()`
* `save_to_file()`
* `load_from_file()`
* `to_dict()`
* `from_dict()`
* Error handling with `try/except`

### What I Learned

This helped me understand the difference between temporary in-memory data and persistent data saved in a file.

Before learning JSON, the data was lost when the program stopped. After adding JSON, the data could be saved and loaded again.

---

### Task 3: Bridge to Data — pandas Introduction

### Folder

```text
week4_pandas_intro/
```

In this task, I started learning pandas, which is used for working with data in table format.

I created a small CSV file with student records, loaded it using pandas, inspected the data, and answered basic questions using filtering and statistics.

### Main Concepts Practiced

* CSV files
* pandas DataFrames
* pandas Series
* `pd.read_csv()`
* `.head()`
* `.info()`
* `.describe()`
* `.shape`
* Filtering rows
* `.mean()`
* `.value_counts()`

### What I Learned

This task helped me understand how Python is used for data-related work, which is important for Artificial Intelligence projects.

---

### Task 4: Mini-Project — Structured Student Analytics Tool

### Folder

```text
week4_student_analytics/
```

In this mini-project, I combined the main concepts I learned into one small working tool.

The project uses OOP classes to manage student and course records, saves and loads data using JSON, exports the records to CSV, and uses pandas to produce student analytics.

### Main Concepts Practiced

* Clean project structure
* Object-oriented programming
* `Student` and `Course` classes
* JSON save and load
* Error handling with `try/except`
* CSV export
* pandas analysis
* Separation of concerns
* Complete README documentation

### Output / Insights

The tool produces basic insights such as:

* Average grade per course
* Top student
* Number of students per course
* Students who scored above 80

### What I Learned

This task helped me understand how different parts of a Python project can work together in one complete mini-project.

It also helped me move from simple programming tasks toward data-related work.

---

## Week 5 — Data Cleaning and Visualization

In Week 5, I started working with more realistic data tasks. The main focus was understanding that real-world data is not always clean and that cleaned data can be understood better using charts.

---

### Task 1: Real Data Is Messy — Data Cleaning with pandas

### Folder

```text
week5_data_cleaning/
```

In this task, I practiced cleaning messy data using pandas.

I used a deliberately messy student CSV file based on my Week 4 student analytics data. The dataset included missing values, duplicate rows, inconsistent text formatting, and wrong data types.

### Main Concepts Practiced

* Loading CSV files using pandas
* Checking dataset information using `.info()`
* Finding missing values using `.isnull().sum()`
* Finding duplicate rows using `.duplicated().sum()`
* Removing duplicates using `.drop_duplicates()`
* Cleaning text using `.str.strip()`, `.str.lower()`, and `.str.title()`
* Fixing numeric data using `pd.to_numeric()`
* Comparing data before and after cleaning

### What I Learned

This task helped me understand that data cleaning is an important step before analysis or machine learning.

Even small problems like extra spaces, missing values, duplicate records, or wrong data types can affect the final result.

---

### Task 2: Seeing the Data — Visualization with matplotlib

### Folder

```text
week5_visualization/
```

In this task, I used the cleaned dataset from the data cleaning task and created charts using matplotlib.

The goal was to understand the data visually instead of only reading it in table form.

### Charts Created

* Bar chart: Average grade per course
* Histogram: Distribution of student grades
* Scatter plot: Student number vs grade
* Bar chart: Number of students per course

### Main Concepts Practiced

* Loading cleaned CSV data
* Using matplotlib for visualization
* Creating bar charts
* Creating histograms
* Creating scatter plots
* Adding chart titles
* Adding x-axis and y-axis labels
* Writing short insights under each chart

### What I Learned

This task helped me understand that visualization makes data easier to read and explain.

A table can show the values, but charts make it easier to notice patterns, comparisons, and distributions. This is useful in data analysis and AI work because we need to understand the data before building any model.

---

## Learning Focus

This internship is helping me improve step by step in:

* Python programming
* C++ basics
* Object-oriented programming
* Git and GitHub workflow
* Project organization
* README writing
* Error handling
* JSON file handling
* CSV file handling
* Data cleaning using pandas
* Basic data analysis using pandas
* Data visualization using matplotlib
* Writing documentation for projects

I am still learning and practicing, but this repository shows my progress through each task.

---

## Current Progress

So far, I have moved from basic programming tasks to more structured Python projects and basic data analysis work.

The internship has helped me understand how coding, file handling, data cleaning, and visualization connect together in practical projects.

---

## Repository Link

```text
https://github.com/haameedfouzaan007-alt/sohail-smart-solutions-internship
```
