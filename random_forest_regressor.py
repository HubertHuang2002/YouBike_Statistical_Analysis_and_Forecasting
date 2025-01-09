import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('YouBikeRent_201707.csv', encoding='utf-8')

df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d', errors='coerce') # Convert 'date' column to datetime format
df = df[df['sarea'] == '中山區']    # Filter data for Zhongshan District ('中山區')
exclude_dates = ['2017-07-29', '2017-07-30']
df = df[~df['date'].isin(pd.to_datetime(exclude_dates))]

# Convert precipitation and temperature to numeric
df['precipitation'] = pd.to_numeric(df['precipitation'], errors='coerce')
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

# Handle missing values (fill with median)
df['precipitation'] = df['precipitation'].fillna(df['precipitation'].median())
df['temperature'] = df['temperature'].fillna(df['temperature'].median())

df['total_rent'] = df['lent'] + df['returned']

# Convert hour and temperature to numeric
df['hour'] = pd.to_numeric(df['hour'], errors='coerce').fillna(0).astype(int)

# Define features (X) and target (y)
X = df[['hour', 'precipitation', 'temperature']]
y = df['total_rent']

# Split into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf = RandomForestRegressor(
    n_estimators=100,    # number of trees
    random_state=42,     # for reproducibility
    n_jobs=-1            # use all available CPU cores
)
rf.fit(X_train, y_train)    # Fit the model on the training data

y_pred = rf.predict(X_test)     # Predict on the test set

# Calculate R-squared and Mean Squared Error
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("Random Forest Regressor Results:")
print(f"R-squared (test): {r2:.4f}")
print(f"MSE (test): {mse:.4f}")
print(f"RMSE (test): {rmse:.4f}")

# Analyze Feature Importance
feature_importances = pd.Series(rf.feature_importances_, index=X.columns)
feature_importances = feature_importances.sort_values(ascending=False)
print("\nFeature Importances:")
print(feature_importances)

# Predicted vs Actual Rentals
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6, color='blue', edgecolor=None)

min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--')
plt.title('Actual vs Predicted Hourly Rentals (Zhongshan District)', fontsize=14)
plt.xlabel('Actual Rentals', fontsize=12)
plt.ylabel('Predicted Rentals', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()