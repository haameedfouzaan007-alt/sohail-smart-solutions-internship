# Week 6 — Model Evaluation

## Task Title

Model Evaluation — Accuracy, Confusion Matrix, and Classification Report

## Task Summary

This task focused on evaluating a trained machine learning model.

In the previous task, I trained a K-Nearest Neighbors model and used it to make predictions. In this task, I checked how good the model really was using accuracy, confusion matrix, and classification report.

The main goal was to understand that a model should not only run successfully. It should also be evaluated honestly.

## Dataset Used

The dataset used in this task is the Iris dataset from scikit-learn.

The dataset contains flower measurements for three Iris flower species:

- Setosa
- Versicolor
- Virginica

## Features and Label

The features, also called X, are:

- sepal length
- sepal width
- petal length
- petal width

The label, also called y, is:

- flower species

## Model Used

The model used in this task is K-Nearest Neighbors.

The first model used:

- `n_neighbors=3`

Then I retrained the model with:

- `n_neighbors=1`

This helped me compare how changing one setting can affect model performance.

## Evaluation Methods Used

The model was evaluated using:

- Accuracy score
- Confusion matrix
- Visual confusion matrix
- Classification report
- Precision and recall interpretation

## Work Completed

- Reviewed why accuracy alone can be misleading
- Learned about confusion matrix
- Learned the basic meaning of precision and recall
- Trained a KNN model
- Calculated model accuracy on the test set
- Created and visualized a confusion matrix
- Printed the classification report
- Retrained the model with a different setting
- Compared the old and new accuracy
- Wrote an honest reflection about whether I would trust the model

## Key Learning

The main thing I learned is that running a model is not enough.

A model must be evaluated properly using test data. Accuracy is useful, but confusion matrix, precision, and recall give a clearer understanding of how the model is performing.