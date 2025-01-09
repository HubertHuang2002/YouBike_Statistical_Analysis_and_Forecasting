import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('YouBikeRent_201707.csv', encoding='utf-8')

df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')  # Convert 'date' column to datetime format
exclude_dates = ['2017-07-29', '2017-07-30']
df = df[~df['date'].isin(pd.to_datetime(exclude_dates))]
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')   # Convert 'temperature' column to numeric format
df['temperature'] = df['temperature'].fillna(df['temperature'].median())    # Handle missing values (fill with median)
df['total_rent'] = df['lent'] + df['returned']

sns.set_theme(style="whitegrid") 
plt.figure(figsize=(12, 6))
sns.scatterplot(
    x='temperature', 
    y='total_rent', 
    data=df, 
    alpha=0.6,     
    edgecolor=None, 
    color='blue'    
)

plt.title('Relationship Between Average Temperature and Total YouBike Rentals for July 2017', fontsize=16)
plt.xlabel('Average Temperature (°C)', fontsize=14)
plt.ylabel('Total Rentals (Lent + Returned)', fontsize=14)

# Set x-axis ticks every 3 degrees
min_temp = df['temperature'].min()
max_temp = df['temperature'].max()
temp_ticks = np.arange(start=np.floor(min_temp / 3) * 3, stop=np.ceil(max_temp / 3) * 3 + 1, step=3)
plt.xticks(ticks=temp_ticks)

plt.grid(True)

plt.tight_layout()
plt.show()