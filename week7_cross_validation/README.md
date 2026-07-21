# Week 7 — Cross-Validation

## Trusting Your Score

This project studies how cross-validation can provide a more reliable machine learning evaluation than one train/test split.

The engineered K-Nearest Neighbors model from the previous feature engineering task was evaluated using 5-fold cross-validation.

## Project Question

Is the accuracy of my engineered KNN model reliable across different parts of the Wine dataset?

## Dataset

The project uses the Wine Classification dataset from scikit-learn.

The dataset contains:

- 178 wine samples
- 13 original numerical features
- 3 target classes
- No missing values

## Model

The model used was K-Nearest Neighbors with:

`n_neighbors=5`

## Feature Engineering

The model used the feature engineering completed in the previous task:

- Numerical feature scaling using StandardScaler
- One-hot encoding for alcohol level
- A new phenol ratio feature

The preprocessing steps and model were placed inside a scikit-learn Pipeline.

## Cross-Validation

The model was evaluated using 5-fold stratified cross-validation.

The dataset was divided into five folds. The model was trained and tested five times, with each fold being used as the test set once.

## Results

| Evaluation | Accuracy |
|---|---:|
| Single Train/Test Split | 100.00% |
| Fold 1 | 97.22% |
| Fold 2 | 91.67% |
| Fold 3 | 100.00% |
| Fold 4 | 97.14% |
| Fold 5 | 100.00% |
| Cross-Validation Mean | 97.21% |
| Standard Deviation | 3.04% |

The cross-validation average was approximately 2.79 percentage points lower than the earlier single-split accuracy.

## Interpretation

I trust the cross-validation average more than the single-split accuracy.

The single-split score was based on only one test group, while cross-validation tested the model using five different sections of the dataset.

The cross-validation result therefore gives a more stable and realistic estimate of the model's performance on unseen data.

## Conclusion

The model continued to perform well across the five folds.

However, the comparison showed that the earlier perfect accuracy was slightly higher than the model's average performance across different data splits.

This task helped me understand why machine learning results should be evaluated using more than one train/test split.

## Files

- `week7_cross_validation.ipynb` — Complete cross-validation notebook
- `README.md` — Project summary and interpretation

## Tools Used

- Python
- Google Colab
- pandas
- NumPy
- scikit-learn
- Git
- GitHub