import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('YouBikeRent_201707.csv', encoding='utf-8')

df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')  # Convert 'date' column to datetime format
exclude_dates = ['2017-07-29', '2017-07-30']    # Exclude data for July 29 and 30
df = df[~df['date'].isin(pd.to_datetime(exclude_dates))]
df['total_rent'] = df['lent'] + df['returned']
daily_total = df.groupby('date')['total_rent'].sum().reset_index()
daily_total['day_of_week'] = daily_total['date'].dt.dayofweek   # Extract day of the week (0=Monday, 6=Sunday)

# Map numerical day to day name
day_mapping = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
daily_total['day_name'] = daily_total['day_of_week'].map(day_mapping)

plt.figure(figsize=(12, 6))
sns.scatterplot(
    x='day_name', 
    y='total_rent', 
    data=daily_total, 
    s=100, 
    color='blue', 
    alpha=0.6
)
plt.title('Daily Total YouBike Rentals and Returns Categorized by Day of the Week for July 2017', fontsize=16)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Total Rentals (Lent + Returned)', fontsize=14)
plt.grid(True)

plt.tight_layout()
plt.show()