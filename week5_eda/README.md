# Week 5 — Exploratory Data Analysis

## Task Overview

In this task, I practiced Exploratory Data Analysis (EDA), which is an important step in any data science or machine learning project. EDA helps us understand the dataset before we start building models or making predictions.

Instead of directly jumping into machine learning, it is important to first explore the data carefully. This includes checking what kind of data we have, identifying missing values, understanding patterns, and finding relationships between different columns.

For this task, I used a real-world cars fuel efficiency dataset. My goal was to explore the dataset and understand how different car features affect fuel efficiency.

In this dataset, fuel efficiency is measured using MPG, which stands for miles per gallon. A higher MPG means the car uses fuel more efficiently, while a lower MPG means the car consumes more fuel.

---

## Main Question

The main question I wanted to answer in this analysis was:

**Do heavier cars have lower fuel efficiency?**

To answer this question, I focused on analyzing the relationship between car weight and MPG. I also explored other related features such as cylinders and horsepower to get a better understanding of how different factors influence fuel efficiency.

---

## Dataset Used

For this task, I used a cars MPG dataset that contains information about different cars and their specifications.

The dataset includes the following columns:

* MPG (Miles per gallon)
* Cylinders (Number of cylinders in the engine)
* Displacement (Engine size)
* Horsepower (Engine power)
* Weight (Weight of the car)
* Acceleration (Acceleration performance)
* Model year (Year the car was made)
* Origin (Country or region of the car)
* Car name (Name of the car)

I chose this dataset because it is simple, easy to understand, and suitable for beginners. It also contains both numeric and categorical data, which makes it useful for practicing different EDA techniques such as summary statistics, grouping, correlation, and visualization.

---

## Files Included

The following files are included in this task:

* `week5_eda.ipynb` — The main notebook where all the analysis is done
* `mpg_cars_dataset.csv` — The dataset used for the analysis
* `README.md` — This file explaining the task and findings

---

## What I Practiced

During this task, I practiced several important EDA steps and techniques:

* Loading a real dataset into a notebook
* Understanding the structure of the dataset (rows, columns, data types)
* Checking for missing values in the dataset
* Cleaning the dataset by removing or handling missing values
* Removing duplicate rows to avoid incorrect analysis
* Standardizing text columns to make the data consistent
* Using `.describe()` to get summary statistics for numeric columns
* Using `.value_counts()` to count how often each category appears
* Using `.groupby()` to compare values across different groups
* Using `.corr()` to understand relationships between numeric columns
* Creating charts to visually explore patterns in the data
* Writing a clear and simple conclusion based on the analysis

---

## Charts Created

To better understand the data, I created several charts:

1. **Weight vs MPG**
   This scatter plot shows the relationship between car weight and MPG. It helps to visually check whether heavier cars tend to have lower fuel efficiency.

2. **Average MPG by Cylinders**
   This bar chart shows the average MPG for cars with different numbers of cylinders. It helps compare fuel efficiency across different engine types.

3. **Horsepower vs MPG**
   This scatter plot shows the relationship between horsepower and MPG. It helps understand whether more powerful cars tend to consume more fuel.

These charts made it easier to identify patterns that are not always obvious from raw data.

---

## Conclusion

From this analysis, I found that heavier cars generally have lower MPG. This means that heavier cars are usually less fuel efficient. The scatter plot between weight and MPG clearly showed a downward trend, where MPG decreases as weight increases.

I also observed that cars with more cylinders tend to have lower average MPG. This is likely because cars with more cylinders are usually larger and require more fuel to operate.

Similarly, cars with higher horsepower also tend to have lower MPG. This suggests that more powerful engines often consume more fuel.

Overall, the analysis shows that weight, number of cylinders, and horsepower are important factors that affect fuel efficiency.

---

## Follow-up Machine Learning Question

Based on the patterns found during EDA, a possible next step would be to build a machine learning model.

A useful question for a future model could be:

**Can we predict a car’s MPG based on its weight, horsepower, cylinders, displacement, and model year?**

This would be a good next step because the EDA showed that these features are strongly related to MPG. A machine learning model could use these features to make predictions about fuel efficiency for new cars.
