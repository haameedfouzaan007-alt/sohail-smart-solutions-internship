# Error Handling & Defensive Programming – Safe Calculator

## Project Overview

This project was completed as part of my Week 2 internship task at Sohail Smart Solutions. The main purpose of this task was to understand error handling and defensive programming in Python.

The program created for this task is a safe calculator named `safe_calculator.py`. It allows the user to perform basic arithmetic operations while handling invalid input and division by zero without crashing.

This task helped me understand that professional software should not only work when the input is correct, but should also handle user mistakes safely.

---

## Project Structure

```text
week2/
└── error-handling/
    ├── safe_calculator.py
    ├── README.md
    ├── reflection.md
    ├── .gitignore
    └── screenshots/
```

---

## Features

The safe calculator supports the following operations:

* Addition
* Subtraction
* Multiplication
* Division

The program also handles:

* Invalid number input
* Division by zero
* Invalid operation input
* Quit command
* Continuous running using a loop

---

## Python Concepts Used

The following Python concepts were applied in this project:

* `try`
* `except`
* `ValueError`
* Conditional statements
* Loops
* User input
* Defensive programming
* Input validation

---

## How the Program Works

The program asks the user to enter:

1. First number
2. Second number
3. Operation

If the user enters text instead of a number, the program displays a friendly error message and continues running.

If the user tries to divide by zero, the program displays a clear message instead of crashing.

The program continues running until the user types:

```text
quit
```

---

## Test Cases

The following test cases were completed:

### Test Case 1 – Valid Calculation

Example:

```text
10 + 5
```

Expected result:

```text
Result: 15.0
```

---

### Test Case 2 – Invalid Input

Example:

```text
abc
```

Expected result:

```text
Invalid number entered. Please try again.
```

---

### Test Case 3 – Division by Zero

Example:

```text
10 / 0
```

Expected result:

```text
Cannot divide by zero. Please try again.
```

---

### Test Case 4 – Quit Command

Example:

```text
quit
```

Expected result:

```text
Exiting calculator. Goodbye!
```

---

## .gitignore

A `.gitignore` file was added to prevent unnecessary files from being uploaded to GitHub.

The `.gitignore` file excludes:

```text
__pycache__/
*.pyc
.vscode/
.idea/
*.log
*.tmp
```

This helps keep the repository clean and professional.

---

## Learning Outcome

Through this task, I learned how exception handling helps prevent Python programs from crashing. I also understood the importance of using `try` and `except` when working with user input.

This project improved my understanding of defensive programming. I learned that good software should expect possible mistakes and handle them in a user-friendly way.

The task also helped me improve my confidence in writing safer and more reliable Python programs.

