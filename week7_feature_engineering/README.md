# Week 7 — Feature Engineering

## Better Inputs, Better Models

This project studies how feature engineering can affect machine learning performance.

The same K-Nearest Neighbors model was trained twice:

1. Using the original raw features
2. Using encoded, scaled and newly created features

Both models used the same train/test split so that the comparison remained fair.

## Project Question

Can feature engineering improve KNN accuracy when predicting the wine class from chemical measurements?

## Dataset

The project uses the Wine Classification dataset from scikit-learn.

The dataset contains:

- 178 wine samples
- 13 original numerical features
- 3 target classes
- No missing values

The features contain chemical measurements such as alcohol, magnesium, total phenols, flavanoids and proline.

## Feature Engineering Steps

### Categorical Feature

An `alcohol_level` column was created by grouping the alcohol values into:

- Low
- Medium
- High

The categories were converted into numerical columns using one-hot encoding.

### Feature Scaling

StandardScaler was applied to the numerical features.

Scaling was important because KNN uses distance, and the Wine dataset contains features with very different value ranges.

### New Feature

A new feature called `phenol_ratio` was created:

`total_phenols / flavanoids`

The purpose was to provide information about the relationship between the two chemical measurements.

## Model

K-Nearest Neighbors was used with:

`n_neighbors=5`

The same model settings and the same train/test split were used for both comparisons.

## Results

| Feature Version | Accuracy |
|---|---:|
| Raw Features | 80.56% |
| Engineered Features | 100.00% |

The engineered model improved by approximately 19.44 percentage points.

## Conclusion

Feature engineering improved the KNN model in this comparison.

The largest improvement was likely caused by feature scaling because KNN is sensitive to differences in numerical scale. Encoding allowed the model to use the categorical alcohol level, and the phenol ratio provided an additional relationship between two existing columns.

This task helped me understand that improving the input features can sometimes be more useful than immediately changing the machine learning algorithm.

## Files

- `week7_feature_engineering.ipynb` — Complete feature engineering notebook
- `README.md` — Project explanation and result summary

## Tools Used

- Python
- Google Colab
- pandas
- NumPy
- scikit-learn
- Git
- GitHub