import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load crime data from a CSV file
crime_data = pd.read_csv('crime_data.csv')

# Select relevant features and target variable
features = ['longitude', 'latitude', 'time_of_day']
target = 'crime_level'
crime_data = crime_data[features + [target]]

# Split data into training and test sets
train_data = crime_data.sample(frac=0.8, random_state=1)
test_data = crime_data.drop(train_data.index)

# Create RandomForestRegressor model and fit to training data
rf_model = RandomForestRegressor(n_estimators=100, random_state=1)
rf_model.fit(train_data[features], train_data[target])

# Generate predictions on test data
predictions = rf_model.predict(test_data[features])

# Evaluate model performance on test data
mse = ((predictions - test_data[target]) ** 2).mean()
print(f"Mean Squared Error: {mse:.2f}")
