import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('YouBikeRent_201707.csv', encoding='utf-8')

df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')  # Convert 'date' column to datetime format
exclude_dates = ['2017-07-29', '2017-07-30']    # Exclude data for July 29 and July 30
df = df[~df['date'].isin(pd.to_datetime(exclude_dates))]
df['precipitation'] = pd.to_numeric(df['precipitation'], errors='coerce')   # Convert 'precipitation' column to numeric format
df['precipitation'] = df['precipitation'].fillna(df['precipitation'].median())  # Handle missing values in 'precipitation' (fill with median)
df['total_rent'] = df['lent'] + df['returned']

sns.set_theme(style="whitegrid") 
plt.figure(figsize=(12, 6))
sns.scatterplot(
    x='precipitation', 
    y='total_rent', 
    data=df, 
    alpha=0.6,     
    edgecolor=None, 
    color='blue'    
)

plt.title('Relationship Between Precipitation and Total YouBike Rentals for July 2017', fontsize=16)
plt.xlabel('Precipitation (mm)', fontsize=14)
plt.ylabel('Total Rentals (Lent + Returned)', fontsize=14)

min_precip = df['precipitation'].min()
max_precip = df['precipitation'].max()
precip_ticks = np.arange(start=np.floor(min_precip / 10) * 10, stop=np.ceil(max_precip / 10) * 10 + 1, step=10)
plt.xticks(ticks=precip_ticks)
plt.grid(True)

plt.tight_layout()
plt.show()