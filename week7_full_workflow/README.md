# Week 7 — Complete Machine Learning Workflow

## Putting It All Together

This project combines the main machine learning skills studied during Week 7:

- Data cleaning
- Feature engineering
- Training multiple models
- Cross-validation
- Model selection
- Final held-out test evaluation

## Project Question

Which beginner machine learning model performs best when predicting the wine class from chemical measurements?

## Dataset

The project uses the Wine Classification dataset from scikit-learn.

The dataset contains:

- 178 wine samples
- 13 original numerical features
- 3 target classes
- No missing values
- No duplicate rows

## Feature Engineering

Two additional features were created.

### Alcohol Level

The numerical alcohol values were grouped into:

- Low
- Medium
- High

The categories were converted into numerical columns using one-hot encoding.

### Phenol Ratio

A new numerical feature was created:

`total_phenols / flavanoids`

The feature represents the relationship between two chemical measurements.

### Feature Scaling

StandardScaler was used to place the numerical features on a comparable scale.

The preprocessing steps were placed inside a Pipeline to prevent data leakage during cross-validation.

## Models Compared

Three classification models were compared:

1. K-Nearest Neighbors
2. Decision Tree
3. Logistic Regression

## Evaluation Method

The dataset was first divided into:

- 80% training data
- 20% held-out test data

The models were compared using 5-fold stratified cross-validation on the training data only.

The held-out test set was not used during model selection.

## Cross-Validation Results

| Model | Mean Accuracy | Standard Deviation |
|---|---:|---:|
| Logistic Regression | 97.88% | 2.85% |
| K-Nearest Neighbors | 95.76% | 2.62% |
| Decision Tree | 89.51% | 5.71% |

## Selected Model

Logistic Regression was selected because it achieved the highest average cross-validation accuracy.

## Final Test Result

The selected model was trained using the complete training set and evaluated on the held-out test set.

| Evaluation | Result |
|---|---:|
| Selected model | Logistic Regression |
| Cross-validation mean | 97.88% |
| Cross-validation standard deviation | 2.85% |
| Held-out test accuracy | 100.00% |

The confusion matrix showed that all 36 held-out test samples were classified correctly for this particular split.

## Conclusion

Logistic Regression performed best in the cross-validation comparison and also achieved a strong result on the final test set.

This workflow showed the importance of improving features, comparing several models fairly, using cross-validation and keeping the final test set separate.

## Limitation

The Wine dataset contains only 178 samples, and the final test set contained only 36 samples.

Because the dataset is small, the perfect test accuracy should not be interpreted as proof that the model will always perform perfectly on new wine data.

The engineered features were also selected manually. Future work could test each feature separately and use a larger external dataset.

## Files

- `week7_full_workflow.ipynb` — Complete machine learning workflow
- `README.md` — Project explanation and result summary

## Tools Used

- Python
- Google Colab
- pandas
- NumPy
- matplotlib
- scikit-learn
- Git
- GitHub