import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load the crime dataset
crime_df = pd.read_csv("crime_dataset.csv")

# Extract the relevant features and target variable
X = crime_df[['latitude', 'longitude', 'crime_type', 'population density' ,'year', 'month' ,'date', 'hours', 'minutes', 'seconds']]
y = crime_df['danger_index']

# Encode categorical features using one-hot encoding
X = pd.get_dummies(X)

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a RandomForestRegressor model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf.predict(X_test)

# Calculate the R-squared score of the model
from sklearn.metrics import r2_score
print("R-squared score:", r2_score(y_test, y_pred))

# Predict the danger index for new localities
new_localities = pd.read_csv("new_localities.csv")
new_X = pd.get_dummies(new_localities[['latitude', 'longitude', 'crime_type', 'month', 'year']])
new_y_pred = rf.predict(new_X)
new_localities['danger_index'] = new_y_pred
print(new_localities[['locality', 'danger_index']])

