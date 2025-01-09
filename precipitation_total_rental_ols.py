import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm

df = pd.read_csv('YouBikeRent_201707.csv', encoding='utf-8')

df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')  # Convert 'date' column to datetime format
exclude_dates = ['2017-07-29', '2017-07-30']    # Exclude data for July 29 and July 30
df = df[~df['date'].isin(pd.to_datetime(exclude_dates))]
df['precipitation'] = pd.to_numeric(df['precipitation'], errors='coerce')   # Convert 'precipitation' column to numeric format
df['precipitation'] = df['precipitation'].fillna(df['precipitation'].median())  # Handle missing values in 'precipitation' (fill with median)
df['total_rent'] = df['lent'] + df['returned']

# Correlation Coefficient and P-value
corr_coeff, p_value = pearsonr(df['precipitation'], df['total_rent'])

# Display correlation and p-value with high precision
print(f"Correlation Coefficient: {corr_coeff:.6f}")
print(f"P-value: {p_value:.6e}")

# Regression Analysis using statsmodels
X = sm.add_constant(df['precipitation'])
y = df['total_rent']
model = sm.OLS(y, X).fit()  # Ordinary Least Squares regression
print(model.summary())