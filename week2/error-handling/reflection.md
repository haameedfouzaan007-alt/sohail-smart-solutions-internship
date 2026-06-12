# Reflection – Error Handling & Defensive Programming

This task helped me better understand why error handling is such an important part of building Python programs. The most common issue I encountered was invalid user input. For example, if a user enters text like `abc` instead of a number, Python cannot convert it into a numeric value. Without proper error handling, this would cause the program to crash.

Using `try` and `except` made the calculator much more reliable because it allowed the program to handle mistakes safely. Instead of displaying confusing Python error messages, the program can show a simple message such as “Invalid number entered. Please try again.” This makes the calculator more user-friendly and easier for anyone to use.

One thing that surprised me was how a small mistake in user input could stop the entire program if it is not handled correctly. I also learned that dividing by zero is a common error that needs special handling because Python cannot perform that calculation.

Defensive programming is important because users do not always enter the correct information. A well-designed program should anticipate possible mistakes and respond appropriately instead of crashing or producing unexpected results.

Compared to my first Python project, I feel much more confident in my programming skills. I am not only learning how to make programs work, but also how to make them more reliable and user-friendly. In future projects, I would like to improve by handling a wider range of errors and creating stronger input validation to make my programs even more robust.
