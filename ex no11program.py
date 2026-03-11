import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report

# For Jupyter notebook visualization
%matplotlib inline

rcParams['figure.figsize'] = 10, 8
sb.set_style('whitegrid')

# Dataset URL
url = "https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic-train.csv"

# Load dataset
titanic = pd.read_csv(url)

# Rename columns
titanic.columns = [
    'PassengerId','Survived','Pclass','Name','Sex',
    'Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'
]

# Display first rows
print(titanic.head())

# Plot survival count
sb.countplot(x='Survived', data=titanic, palette='hls')
plt.show()

# Check missing values
print(titanic.isnull().sum())

# Dataset information
print(titanic.info())
