#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats

# stats.f_oneway function takes groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(df['A'], df['B'], df['C'], df['D'])
print(fvalue, pvalue)
# Example output:
# 17.492810457516338 2.639241146210922e-05


# Get ANOVA table similar to R output
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(treatments)', data=df_melt).fit()

anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)


# In[3]:


# Impor# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score, KFold

import warnings
warnings.filterwarnings('ignore')

# Load dataset
housing = pd.read_csv("Housing.csv")

# Select required columns
df = housing[['area','price']]

# Scaling
scaler = MinMaxScaler()
df[['area','price']] = scaler.fit_transform(df[['area','price']])

# Visualization
sns.regplot(x="area", y="price", data=df, fit_reg=False)
plt.show()

# Train-test split
df_train, df_test = train_test_split(df, train_size=0.7, test_size=0.3, random_state=10)

# Split X and y
X_train = df_train['area'].values.reshape(-1,1)
y_train = df_train['price']

X_test = df_test['area'].values.reshape(-1,1)
y_test = df_test['price']

# Polynomial Regression Model
degree = 2
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Cross Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=10)
scores = cross_val_score(model, X_train, y_train, cv=kfold, scoring='r2')

# Results
print("Cross Validation Scores:", scores)
print("Average R2 Score:", scores.mean())

# Plot predictions
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel("Area")
plt.ylabel("Price")
plt.legend()
plt.show()


# In[8]:


# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score, KFold

import warnings
warnings.filterwarnings('ignore')

# Load dataset
housing = pd.read_csv(r"C:\Users\AIDS\Documents\housing.csv")

# Select required columns
df = housing[['area','price']]

# Scaling
scaler = MinMaxScaler()
df[['area','price']] = scaler.fit_transform(df[['area','price']])

# Visualization
sns.regplot(x="area", y="price", data=df, fit_reg=False)
plt.show()

# Train-test split
df_train, df_test = train_test_split(df, train_size=0.7, test_size=0.3, random_state=10)

# Split X and y
X_train = df_train['area'].values.reshape(-1,1)
y_train = df_train['price']

X_test = df_test['area'].values.reshape(-1,1)
y_test = df_test['price']

# Polynomial Regression Model
degree = 2
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Cross Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=10)
scores = cross_val_score(model, X_train, y_train, cv=kfold, scoring='r2')

# Results
print("Cross Validation Scores:", scores)
print("Average R2 Score:", scores.mean())

# Plot predictions
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel("Area")
plt.ylabel("Price")
plt.legend()
plt.show()


# In[ ]:




