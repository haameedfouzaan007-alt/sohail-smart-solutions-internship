# README Documentation – Functions, Modules & Reusable Code

## Project Overview

This project was completed as part of my Week 2 internship task at Sohail Smart Solutions. The purpose of this task was to understand how Python programs can be organized in a cleaner and more professional way using functions and modules.

In my previous Python tasks, most of the code was written in a single file. In this task, I learned how to separate reusable logic into another Python file. This makes the program easier to read, test, maintain, and reuse in future projects.

The project uses two main Python files: `student_utils.py` and `main.py`. The `student_utils.py` file contains reusable student-related functions, while `main.py` imports and uses those functions to test the program.

---

## Project Structure

```text
week2/
└── functions-module/
    ├── main.py
    ├── student_utils.py
    ├── README.md
    └── screenshots/
```

---

## Files Included

## main.py

The `main.py` file is the main program file. It imports the `student_utils` module and uses the functions from that file. It also creates sample student data and displays the output of each test case.

## student_utils.py

The `student_utils.py` file contains reusable functions related to student records. These functions are kept separate from the main program so that the code is more organized and easier to reuse.

## README.md

The `README.md` file explains the purpose of the project, the project structure, the functions used, how to run the program, and the learning outcome.

## screenshots/

The `screenshots` folder contains evidence of the program execution and output.

---

## Functions Used

This project includes three reusable functions.

## find_student(students, name)

This function searches for a student by name. If the student exists, it returns the university name. If the student does not exist, it returns `None`.

## add_student(students, name, university)

This function adds a new student record to the student dictionary. It takes the student name and university as input and returns the updated dictionary.

## unique_universities(students)

This function returns a set of unique universities from the student records. It helps avoid duplicate university names in the output.

---

## Python Concepts Applied

The following Python concepts were used in this project:

* Functions
* Parameters
* Return values
* Modules
* Import statement
* Dictionaries
* Sets
* Docstrings
* Code organization
* Reusable code

---

## How to Run the Program

To run the program, open the project folder and execute the following command:

```bash
python main.py
```

The program will run the test cases and display the results in the terminal.

---

## Output Evidence

The program was executed once, and the output screenshot shows all four required test cases in a single run.

The program was tested by running `main.py`. Each reusable function was tested at least once through the output shown in the terminal.

---

### Test Case 1 – Student Exists

The program searched for an existing student named `Haameed`.

**Expected Result:** The program should return the university name.

**Actual Result:** `Haameed studies at: AURAK`

**Status:** Passed

---

### Test Case 2 – Student Does Not Exist

The program searched for a student named `Omar`, who was not available in the sample data.

**Expected Result:** The program should show that the student was not found.

**Actual Result:** `Student not found.`

**Status:** Passed

---

### Test Case 3 – New Student is Added

The program added a new student named `Mariam` with the university `Khalifa University`.

**Expected Result:** The updated student records should include Mariam.

**Actual Result:** The updated dictionary included `Mariam: Khalifa University`.

**Status:** Passed

---

### Test Case 4 – Unique Universities Displayed

The program displayed all unique universities from the student records.

**Expected Result:** Repeated university names should not be duplicated.

**Actual Result:** The program displayed unique universities including `AURAK`, `University of Sharjah`, and `Khalifa University`.

**Status:** Passed


## Learning Outcome

Through this task, I learned how to organize Python code using functions and modules. I understood that writing all code in one long file can make a program harder to manage, especially as the project becomes bigger.

I also learned the importance of returning values from functions instead of only printing them. Returning values make the code more reusable because the result can be stored, processed, or used by another function.

This task helped me understand how professional Python projects are structured. It also improved my understanding of docstrings, reusable functions, and clean project organization. These concepts will be useful in future Python, Data Science, Machine Learning, and AI-related projects.
