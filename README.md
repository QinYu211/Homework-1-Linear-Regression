# Homework 1: Linear Regression

This homework covers several regression topics, and will give you practive with numpy and sklearn libraries in Python. It has both a coding and a writing component.

## Goals

In this homework you will:
  1. Build linear regression models to serve as predictors from input data.
  2. Parse input data into feature matrices and target variables.
  3. Find the best regularization parameter for a dataset.

## Background

Before attempting the homework, please review the notes on regression. In addition to what is covered there, the following background may be useful:

### CSV Processing in Python

Like .txt, .csv (comma-separated values) is a useful file format for storing data. In a CSV file, each line is a data record, and different fields of the record are separated by commas, making them two-dimensional data tables (i.e. records by fields). Typically, the first row and first column are headings for the fields and records.
Python's pandas module helps manage two-dimensional data tables. We can read a CSV as follows:
```
import pandas as pd
data = pd.read_csv('data.csv')
```
To see a small snippet of the data, including the headers, we can write `data.head()`. Once we know which columns we want to use as features (say 'A','B','D') and which to use as a target variable (say 'C'), we can build our feature matrix and target vector by referencing the header:
```
X = data[['A', 'B', 'D']]
y = data[['C']]
```
More details on `pandas.read_csv()` can be found [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

### Matrix Algebra in Python

Python offers computationally efficient functions for linear algebra operations through the numpy library. Suppose `A` is a list of _m_ lists, each having _n_ numerical items. Numpy will treat `A` as an _m x n_ matrix. If we want to transpose `A`, we can write:
```
import numpy as np
AT = A.T
```
If `B` is another _m x n_ matrix, we can perform the matrix operation _A<sup>T</sup>B_ by writing: (Note that if n = 1, i.e. `A` and `B` are both vectors with _m_ elements, this operation takes the dot product between the vectors)
```
AB = A.T @ B
```

If `A` is a square _n x n_ matrix, we can find its inverse (if it exists) with the following:
```
Ainv = np.linalg.inv(A)
```
Other useful matrix operations can be found [here](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html).

### Linear Regression in Python

Python offers several standard machine learning models with optimized implementations in the sklearn library. Suppose we have a feature matrix `X` and a target variable vector `y`. To train a standard linear regression model, we can write:
```
from sklearn.linear_model import LinearRegression
model_lin = LinearRegression(fit_intercept = True)
model_lin.fit(X, y)
```
Then, if we have a feature matrix `Xn` of new samples, we can predict the target variables (if we know the model is performing well) by applying the trained model:
```
yn = model_lin.predict(Xn)
```
And we can view the parameters of the model by writing:
```
model_lin.get_params()
```
There are also a few different versions of regularized linear regression models in sklearn. One of the most common is Ridge Regression, which has a single regularization parameter λ. To train with λ = 0.2, for instance, we can write:
```
from sklearn.linear_model import Ridge
model_ridge = Ridge(alpha = 0.2, fit_intercept = True)
model_ridge.fit(X, y)
```
More regression models in Python can be found [here](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning.).

## Instructions

### Setting Up Your Repository
Click the link on Brightspace to set up your repository for Homework 1, then clone it.
Aside from this README, the repository should contain the following files:
  1. `polyfit.py` - A starter file with instructions, functions, and a skeleton that you will fill out in Problem 1.
  2. `poly.txt` - A data file for Problem 1, where each row is a datapoint in the format: `x y`, with `x` being the explanatory and `y` being the target variable.
  3. `regularize-cv.py` - A starter file with instructions, functions, and a skeleton that you will fill out in Problem 2.
  4. `diamonds.csv` - A data file for Problem 2, where each row has 10 attributes corresponding to a diamond.
  5. `problem1_writeup_sample.pdf` - A sample writeup for Problem 1. You need to include everything that is shown in the sample writeup.
  6. `problem2_writeup_sample.pdf` - A sample writeup for Problem 2. You need to include everything that is shown in the sample writeup.
  
### Problem 1: Polynomial Regression
A common misconception is that linear regression can only be used to fit a linear relationship. We can fit more complicated functions of the explanatory variables by defining new features that are functions of the existing features. A common class of models is the **polynomial**, with a _d_ th degree polynomial being of the form:

_&#375;<sub>d</sub>(x) = a<sub>d</sub>x<sup>d</sup>+a<sub>d-1</sub>x<sup>d-1</sup>+...+a<sub>2</sub>x<sup>2</sup>+a<sub>1</sub>x<sup>1</sup>+b_

The polynomial has _d_ + 1 parameters: _β = (a<sub>d</sub>, ..., a<sub>1</sub>, b)<sup>T</sup>_. 

So _d_ = 1 corresponds to a line, _d_ = 2 to a quadratic, _d_ = 3 to a cubic, and so forth.

In this problem, you will build a series of functions that fit polynomials of different degrees to a dataset. You will then use this to determine the best fit to a dataset by comparing the models from different degrees visually against a scatterplot of the data. More specifically:

  1. Complete the functions in `polyfit.py`, which accepts as input a dataset to be fit and polynomial degrees to be tried, and outputs a list of fitted models. The specifications for the `main`, `feature_matrix`, and `least_squares` functions are contained as comments in the skeleton code. The key steps include parsing the input data, creating the feature matrix, and solving the least squares equations.
  2. Use your completed `polyfit.py` to find fitted polynomial coefficients for _d_ = 1,2,3,4,5 on the `poly.txt` dataset. Write out the resulting estimated functions _&#375;<sub>d</sub>(x)_ for each _d_ in your writeup.
  3. Use your fitted polynomial coefficients to fill in the coefficients of each coefficient list in `main`. Notice you will also need to replace the fake data with the real data from the datapath. We are using the `scatter` and `plot` functions in the `matplotlib.pyplot` module to visualize the dataset and these fitted models on a single graph. What degree polynomial does the relationship seem to follow? Explain in your writeup.

Note that in this problem, **you are not permitted to use the `sklearn` library**. You must use matrix operations in numpy to solve the least squares equations.

Once you have completed `polyfit.py`, if you run the test case provided, it should output (rounded to 6
significant digits):
[[7.00158, 9.30386, -239.334], [0.00598796, 0.755218, 0.234560, 1.17636, -175.880]]

### Problem 2: Regularized Regression
Regularization techniques like Ridge Regression introduce an extra model parameter, namely, the regularization parameter λ. To determine the best value of λ for a given dataset, we often employ cross validation, where we compare the error of the trained model with different values of λ on a test set, and choose the one yielding the lowest error.

In this problem, you will complete the starter code `regularize-cv.py` that employs cross validation in selecting the best combination of model parameters β and regularization parameter λ for a predictor on a given dataset. We use the `diamonds.csv` dataset (taken from the "Prices of over 50,000 round cut diamonds" dataset [here](http://vincentarelbundock.github.io/Rdatasets/datasets.html)), which contains the prices and nine descriptive attributes (carats, cut, color, clarity, depth, table, x, y, z) of roughly 54,000 diamonds. From the input data, you will train a Ridge Regression model on these nine attributes for different values of λ, find the best, and use the result to predict the price of a new diamond given a set of input features describing it. More specifically:

  1. Complete the function `normalize.test` that takes the testing set **X_test** and the training set means and standard deviations and returns a normalized feature matrix. Each column should subtract the mean of the corresponding column from **X_train** and divide by the standard deviation of the corresponding column from **X_train**. For example, each element in the first column of **X_test** should subtract the mean of the first column of **X_train** and divide by the standard deviation of the first column of **X_train**.
  2. Complete the function `train_model` to fit a Ridge Regression model with regularization parameter λ = l on the training dataset. You may use the `linear_model.Ridge` class in sklearn to do this. Note that the partition of the training and testing set has already been done for you in the `main` function.
  3. Complete the function `error` to calculate the mean squared error of the model on the testing dataset.
  4. Complete the code in `main` for plotting the mean squared error as a function of λ, and for finding the model and mse corresponding to the best lmbda. Be sure to include a title and axes labels with your plot. Add the output message and plot to your writeup.
  5. Using the coefficients (and intercept) _β = (a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>9</sub>, b)<sup>T</sup>_ from the returned `model_best`, write out the equation of your fitted model for a sample **x** in your writeup. What is the predicted price y for a 0.25 carat, 3 cut, 3 color, 5 clarity, 60 depth, 55 table, 4 x, 3 y, 2 z diamond?
  
Once you have completed `regularize-cv.py`, if you set `lmbda = [1,100]`, your output message should be:
'Best lambda tested is 1, which yields an MSE of 1812351.1908771885'.

## What to Submit
For each problem, you must submit:
  1. Your completed version of the starter code
  2. A writeup as a separate PDF document named `problem1_writeup.pdf` and `problem2_writeup.pdf` respectively. Sample writeups are available in your GitHub.

## Submitting Your Code
Push your completed `polyfit.py`, `problem1_writeup.pdf`, `regularize-cv.py`, and `problem2_writeup.pdf` to your repository before the deadline.
