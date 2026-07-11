# Week 6 — First ML Mini-Project

## Project Title

Iris Flower Species Prediction

## Task Summary

This project is my first complete end-to-end machine learning mini-project.

The goal was to build a simple machine learning pipeline from data understanding to model evaluation.

The full process included:

- Understanding the dataset
- Checking and preparing the data
- Identifying X and y
- Splitting the data into training and test sets
- Training a simple model
- Making predictions
- Evaluating the model
- Writing an honest conclusion

## Dataset Used

The dataset used in this project is the Iris dataset from scikit-learn.

The dataset contains measurements of Iris flowers.

The flower species are:

- Setosa
- Versicolor
- Virginica

## Project Question

Can I predict the Iris flower species from sepal and petal measurements?

## Task Type

This is a classification task because the model predicts a category.

The category is the flower species.

## Features and Label

The features, also called X, are:

- sepal length
- sepal width
- petal length
- petal width

The label, also called y, is:

- flower species

## Model Used

The model used in this project is K-Nearest Neighbors.

I used:

- `n_neighbors=3`

KNN predicts based on nearby examples from the training data.

## Evaluation Methods

The model was evaluated using:

- Accuracy score
- Confusion matrix
- Classification report
- Precision and recall
- Training vs test accuracy comparison

## Result

The model performed very well on the Iris test data.

The accuracy was high, and the confusion matrix showed that the model correctly predicted most or all flower species.

## Limitation

One limitation is that the Iris dataset is small and already clean.

Because of this, the model may perform very well here, but real-world datasets can be more difficult, messy, and less balanced.

## Future Improvement

In the future, I can improve this project by trying other models such as Decision Tree or Logistic Regression and comparing their results.

I can also try a larger or more realistic dataset.