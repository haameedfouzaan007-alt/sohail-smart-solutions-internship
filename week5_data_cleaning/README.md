# Week 5 — Data Cleaning with pandas

## Task Overview

This task is about learning how to clean messy real-world data using pandas.

Last week, I worked with clean and structured student data. In this task, I practiced what happens when the data is not clean. Real-world datasets can have missing values, duplicate rows, inconsistent text formatting, and wrong data types. If these problems are not fixed, they can affect the final analysis and even machine learning results.

For this task, I created a deliberately messy student CSV file based on my Week 4 student analytics data and cleaned it step by step using pandas.

## Files Included

* `week5_data_cleaning.ipynb`
* `messy_students.csv`
* `cleaned_students.csv`
* `README.md`

## Dataset Used

I used a student dataset with the following columns:

* Student ID
* Name
* University
* Course
* Grade

The messy dataset included common data problems such as:

* Missing student name
* Missing university value
* Missing grade
* Duplicate student record
* Extra spaces in text values
* Different capitalization in names, university, and course values
* One grade written as text instead of a number

## What I Practiced

In this task, I practiced using pandas for data cleaning, including:

* Loading CSV data using `pd.read_csv()`
* Checking dataset information using `.info()`
* Finding missing values using `.isnull().sum()`
* Finding duplicate rows using `.duplicated().sum()`
* Removing duplicates using `.drop_duplicates()`
* Cleaning text using `.str.strip()`, `.str.lower()`, and `.str.title()`
* Fixing data types using `pd.to_numeric()`
* Comparing the dataset before and after cleaning

## Cleaning Steps Completed

### 1. Handling Missing Values

I checked for missing values in each column.

The row with a missing student name was removed because the student could not be identified properly.

For the missing university value, I filled it with `Unknown` because it was a text column and did not directly affect the grade analysis.

For the missing grade value (Yousef’s grade), I filled it with the average grade. This was done only for learning and practicing data cleaning techniques. In real-world scenarios, it is not always appropriate to replace a student's actual grade with an average, but for this task it helped demonstrate how to handle missing numeric values.

### 2. Removing Duplicates

I found and removed duplicate rows from the dataset.

This was important because duplicate records can affect student counts and average grade calculations.

### 3. Standardizing Text Columns

Some text values had extra spaces and different capitalization.

For example:

* `haameed` was cleaned to `Haameed`
* `aurak` was cleaned to `AURAK`
* `python oop` was cleaned to `Python OOP`

This made the dataset more consistent and easier to analyze.

### 4. Fixing Data Types

The grade column had one value written as text: `seventy four`.

I changed it to `74` and converted the grade column into a numeric data type using `pd.to_numeric()`.

This was important because grades must be numbers for calculations like average grade.

## The 3 Cleaning Steps That Mattered Most

1. **Handling missing values**
   Missing values were important to fix because they can make the dataset incomplete and affect the final analysis.

2. **Removing duplicates**
   Duplicate rows can make student counts and averages incorrect, so removing them made the dataset more accurate.

3. **Standardizing text and fixing data types**
   Text values needed to be consistent, and grades needed to be numeric for proper calculations.

## Reflection

This task helped me understand that real-world data is usually not clean. Before doing analysis or machine learning, the data needs to be checked and cleaned properly.

I also learned that even small problems like extra spaces, duplicate rows, and wrong data types can affect the final result. This task was useful because it showed me the importance of cleaning data before using it for analysis.
