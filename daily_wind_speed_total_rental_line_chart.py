import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('YouBikeRent_201707.csv', encoding='utf-8')

df['date'] = pd.to_datetime(df['date']) # Convert 'date' column to datetime format
df['wind_speed'] = pd.to_numeric(df['wind_speed'], errors='coerce') # Convert 'wind_speed' column to numeric (if necessary)
df['wind_speed'] = df['wind_speed'].fillna(df['wind_speed'].median())
daily_avg_wind = df.groupby('date')['wind_speed'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(daily_avg_wind['date'], daily_avg_wind['wind_speed'], marker='o', linestyle='-', color='blue')

plt.title('Daily Average Wind Speed for July 2017', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Average Wind Speed (m/s)', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()