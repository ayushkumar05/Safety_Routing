from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import numpy as np


def load_data():

    # code to load the preprocessed data from the file
    pass

def engineer_features(crime_data, weather_data, road_data):
    # Crime statistics features
    crime_features = []
    for crime_type in ["violent_crime", "property_crime", "drug_crime"]:
        total_crime_type = sum(crime_data[crime_type])
        crime_features.append(total_crime_type)
        
    # Weather report features
    weather_features = []
    for weather_type in ["temperature", "humidity", "precipitation"]:
        average_weather_type = np.mean(weather_data[weather_type])
        weather_features.append(average_weather_type)
        
    # Road data features
    road_features = []
    for road_type in ["speed_limit", "lanes", "road_condition"]:
        average_road_type = np.mean(road_data[road_type])
        road_features.append(average_road_type)
        
    # Concatenate all features into a single feature vector
    feature_vector = crime_features + weather_features + road_features
    
    return feature_vector

def train_model(data):
    # Engineer features
    data = engineer_features(data)
    
    # Split data into training and testing sets
    train_data = data.sample(frac=0.8, random_state=42)
    test_data = data.drop(train_data.index)

    # Define features and labels
    features = ['crime_rate', 'temperature', 'precipitation', 'road_quality']
    label = 'risk_score'

    # Train random forest regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(train_data[features], train_data[label])

    # Evaluate model
    train_rmse = evaluate_model(model, train_data, features, label)
    test_rmse = evaluate_model(model, test_data, features, label)
    
    print(f"Train RMSE: {train_rmse:.2f}")
    print(f"Test RMSE: {test_rmse:.2f}")

    return model

def evaluate_model(model, data, features, label):
    predictions = model.predict(data[features])
    #update function usage
    mse = mean_squared_error(predictions, data[label])
    rmse = np.sqrt(mse)
    return rmse

def predict_risk(model, route_data):
    # Engineer features
    route_data = engineer_features(route_data)

    # Predict risk score
    features = ['crime_rate', 'temperature', 'precipitation', 'road_quality']
    risk_score = model.predict(route_data[features])

    return risk_score


def preprocess_data():
    # code to preprocess the data and split it into training and testing sets
    pass



def save_model():
    # code to save the trained model to a file
    pass

if __name__ == '__main__':
    data = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(data)
    model = train_model(X_train, y_train)
    save_model(model)
