# Week 7 — Comparing Multiple Machine Learning Models

## Task Overview

This project compares three beginner machine learning classification models using the Iris dataset.

The three models are:

1. K-Nearest Neighbors
2. Decision Tree
3. Logistic Regression

The purpose of the task is to understand why one model should not be trusted without comparing it with other models.

## Dataset

The project uses the Iris dataset from scikit-learn.

The input features are:

* Sepal length
* Sepal width
* Petal length
* Petal width

The target is the Iris flower species:

* Setosa
* Versicolor
* Virginica

## Train/Test Split

The dataset was divided into:

* 80% training data
* 20% testing data

The same train/test split was reused for all three models to make the comparison fair.

## Baseline

A simple baseline model was created using the most common class strategy.

The baseline achieved approximately 33.33% accuracy. All three machine learning models performed better than the baseline.

## Models and Results

| Model               | Accuracy |
| ------------------- | -------: |
| K-Nearest Neighbors |  100.00% |
| Logistic Regression |   96.67% |
| Decision Tree       |   93.33% |

## Conclusion

K-Nearest Neighbors achieved the highest accuracy in this comparison.

It performed 3.33 percentage points better than Logistic Regression, which was the second-best model.

My guess is that KNN suited the Iris dataset because flowers belonging to the same species usually have similar sepal and petal measurements.

This result does not mean that KNN is always the best model. Different datasets may produce different results, so comparing multiple models is important before selecting a final model.

## Files

* `week7_model_comparison.ipynb` — Colab notebook containing the complete model comparison
* `README.md` — Project explanation and result summary

## Tools Used

* Python
* Google Colab
* pandas
* scikit-learn
* GitHub
