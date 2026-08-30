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

X → Temperature (°C)<br />
y → Ice Cream Sales (units)

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

Mean Squared Error (MSE): ```107.5207```<br />
R² Score: ```-0.0256```<br />

The negative R² score shows that a simple straight-line model does not fit this dataset well.

**Example Prediction**

For a temperature of 30°C, Linear Regression predicted approximately: ```3.42 units```

## 📉 Polynomial Regression

Because the relationship between temperature and sales is non-linear, Polynomial Regression was applied.

PolynomialFeatures(degree=2)
