# Week 5 EDA Mini-Project — One Clean Data Story

## Project Overview

This project is a complete Exploratory Data Analysis (EDA) mini-project where I worked with a cars fuel efficiency dataset. The main idea behind this project was not just to write code, but to turn the dataset into a meaningful and easy-to-understand data story.

Instead of simply running commands and generating outputs, I focused on asking a clear question, understanding the dataset, cleaning it properly, analyzing patterns, creating visualizations, and finally explaining what the results actually mean. This approach helped me move beyond just coding and start thinking like a data analyst.

Through this project, I applied the key skills I learned during Week 5, including data cleaning, summarizing data, creating visualizations, and organizing an analysis in a logical and readable flow.

---

## Main Question

The main question I explored in this project is:

**Do heavier and more powerful cars have lower fuel efficiency?**

In this dataset, fuel efficiency is measured using MPG (miles per gallon). A higher MPG means the car can travel more distance using less fuel, which makes it more efficient.

This question helped guide the entire analysis, as I focused on understanding how features like weight, horsepower, and cylinders are related to MPG.

---

## Dataset Used

For this project, I used a cars MPG dataset that contains detailed information about different cars and their specifications.

The dataset includes the following columns:

* MPG (miles per gallon)
* Cylinders
* Displacement
* Horsepower
* Weight
* Acceleration
* Model year
* Origin
* Car name

I chose this dataset because it is beginner-friendly and easy to understand. At the same time, it contains enough useful numeric data to explore meaningful relationships, especially when analyzing fuel efficiency.

---

## Files Included

The project folder contains the following files:

* `week5_eda_project.ipynb` — The main notebook where all the analysis is done
* `mpg_cars_dataset.csv` — The dataset used for the project
* `README.md` — This file, which explains the project

---

## What the Notebook Includes

The notebook is organized in a clear and structured way so that anyone can follow the analysis step by step. It includes:

1. An introduction and the main question
2. Learning notes about what makes a good data story
3. Understanding the dataset (shape, columns, missing values, etc.)
4. A cleaning section where the data is prepared for analysis
5. An analysis section using `.describe()`, `.value_counts()`, and `.groupby()`
6. A correlation check to understand relationships between numeric features
7. A visualization section with clearly labeled charts
8. A short insight written after each chart
9. A final conclusion with three key findings
10. A follow-up machine learning question

This structure helps make the notebook easy to read and understand, even for someone who is not deeply familiar with coding.

---

## Cleaning Steps

Before starting the analysis, I cleaned the dataset to make sure the results would be accurate and reliable.

First, I noticed that there were some missing values in the `horsepower` column. Since horsepower is an important feature for answering the main question, I decided to remove the rows where this value was missing instead of filling them with guesses.

Next, I checked for duplicate rows and removed them if any were found. Duplicate data can affect the results and lead to incorrect conclusions.

I also cleaned the text columns such as `origin` and `name` by removing extra spaces and making the formatting consistent. This step helps avoid confusion when grouping or analyzing the data.

Overall, cleaning the dataset was an important step because messy or incomplete data can lead to misleading results.

---

## Charts Created

To better understand the relationships in the data, I created several charts. Each chart helps answer a part of the main question.

1. **Weight vs MPG**
   This scatter plot shows the relationship between a car’s weight and its fuel efficiency. From the chart, it is clear that heavier cars tend to have lower MPG.

2. **Average MPG by Cylinders**
   This bar chart compares the average MPG for cars with different numbers of cylinders. It shows that cars with fewer cylinders generally have better fuel efficiency.

3. **Horsepower vs MPG**
   This scatter plot shows how horsepower is related to MPG. The chart indicates that cars with higher horsepower usually have lower MPG.

4. **Average MPG by Origin**
   This bar chart compares fuel efficiency across cars from different regions. It shows that cars from different origins have different average MPG values, suggesting that origin may also play a role in fuel efficiency.

---

## Key Findings

After analyzing the data and reviewing the charts, I found three main insights:

1. **Heavier cars usually have lower fuel efficiency.**
   The relationship between weight and MPG shows a clear pattern where MPG decreases as weight increases.

2. **Cars with more cylinders tend to have lower average MPG.**
   Vehicles with fewer cylinders are generally more fuel efficient compared to those with more cylinders.

3. **Higher horsepower is associated with lower MPG.**
   More powerful cars often consume more fuel, which results in lower fuel efficiency.

Overall, these findings suggest that weight, cylinders, and horsepower are key factors that influence how fuel efficient a car is.

---

## Follow-up Machine Learning Question

Based on the insights from this analysis, a useful next step would be to build a machine learning model to answer the following question:

**Can we predict a car’s MPG based on its weight, horsepower, cylinders, displacement, and model year?**

This would be a valuable extension of the project because the EDA already showed that these features are strongly related to MPG.

---

## Reflection

This project helped me understand that a good notebook is not just about writing code that works. It should also clearly explain the purpose of the analysis, show each step in a logical order, and communicate the results in a simple and meaningful way.

I also learned that visualizations are much more powerful when they are connected to a clear question and followed by a short explanation. This makes it easier for anyone reading the notebook to understand the insights without needing to analyze the charts deeply.

Overall, this project helped me improve both my technical skills and my ability to present data in a clear and human-friendly way.
