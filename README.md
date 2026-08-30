# 🍦 Ice Cream Sales Prediction using Machine Learning

## 📌 Project Overview

This project predicts Ice Cream Sales based on Temperature (°C) using Machine Learning regression techniques.

The project compares:
- **Linear Regression**
- **Polynomial Regression (Degree = 2)**

The goal is to find which model fits the temperature-sales relationship better.

## 📊 Dataset
File: ```Ice_cream_selling_data.csv```
- Total Records: 49
- Total Features: 1
- Input Feature: ```Temperature (°C)```
- Target Variable: ```Ice Cream Sales (units)```

**Feature and Target**

- X → Temperature (°C)<br />
- y → Ice Cream Sales (units)

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## 📈 Linear Regression

Linear Regression was first used to model the relationship between temperature and ice cream sales.

**Results**

- Mean Squared Error (MSE): ```107.5207```<br />
- R² Score: ```-0.0256```<br />

The negative R² score shows that a simple straight-line model does not fit this dataset well.

**Example Prediction**

- For a temperature of 30°C, Linear Regression predicted approximately: ```3.42 units```

## 📉 Polynomial Regression

Because the relationship between temperature and sales is non-linear, Polynomial Regression was applied.

PolynomialFeatures(degree=2)

**Results**

- Training R² Score: ```0.9385```
- Test Mean Squared Error (MSE): ```13.0868```
- Test R² Score: ```0.8752```

Polynomial Regression performs much better than Linear Regression on the test data.

## 🏆 Model Comparison

| Model | Test MSE | Test R² Score |
|---|---:|---:|
| Linear Regression | 107.5207 | -0.0256 |
| **Polynomial Regression** | **13.0868** | **0.8752** |

## Best Model

**Polynomial Regression (Degree = 2) is the best-performing model in this project.**

It achieved a test R² score of approximately 87.52% and a much lower prediction error compared with Linear Regression.

## 📊 Visualization

The project includes:

- Temperature vs Ice Cream Sales scatter plot
- Linear Regression prediction line
- Polynomial Regression prediction curve

These visualizations help show why Polynomial Regression fits the dataset better.


## ✅ Conclusion

The project shows that the relationship between temperature and ice cream sales is better captured by a non-linear model.


Linear Regression produced a negative R² score on the test set, while Polynomial Regression achieved an R² score of 0.8752 with a substantially lower MSE.


Therefore, **Polynomial Regression was selected as the better model for this dataset.**


## 🚀 Future Improvements

- Test different polynomial degrees
- Compare additional regression algorithms
- Perform cross-validation
- Add hyperparameter tuning
- Build a simple Streamlit web application
- Deploy the model online
