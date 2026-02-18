EX NO:2A

import pandas as pd

# list of strings
lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)

print(df)

EX NO:2B
import pandas as pd

# initialise data of lists
data = {
    'Name': ['Tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output
print(df)

EX NO:2C

import pandas as pd

# Define a dictionary containing employee data
data = {
    'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32],
    'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd']
}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

print(df)

# Select two columns
print(df[['Name', 'Qualification']])

EX NO:2D

# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
data = {
    'First Score': [100, 90, np.nan, 95],
    'Second Score': [30, 45, 56, np.nan],
    'Third Score': [np.nan, 40, 80, 98]
}

# creating a dataframe
df = pd.DataFrame(data)

# using isnull() function
print(df.isnull())
