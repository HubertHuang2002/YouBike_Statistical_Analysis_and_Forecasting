import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('YouBikeRent_201707.csv', encoding='utf-8')

df['date'] = pd.to_datetime(df['date']) # Convert 'date' column to datetime format
df['total_rent'] = df['lent'] + df['returned']
daily_total = df.groupby('hour')['total_rent'].sum().reset_index()  # Group by date and sum the total rentals

plt.figure(figsize=(12, 6))
plt.plot(daily_total['hour'], daily_total['total_rent'], marker='o', linestyle='-', color='b')

plt.title('Hourly Total YouBike Rentals and Returns for July 2017')
plt.xlabel('Hour')
plt.ylabel('Total Rentals (Lent + Returned)')
plt.xticks(ticks=range(24))
plt.grid(True)

plt.tight_layout()
plt.show()