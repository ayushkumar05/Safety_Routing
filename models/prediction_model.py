#crime statistics
import joblib
import pandas as pd

def load_model():
    # code to load the trained model from a file
    pass


import requests
import json

def load_route_data(start_coords, end_coords, mode="car", api_key=None):
    """
    Loads route data using the OpenRouteService API.

    Parameters:
        start_coords (tuple): The (latitude, longitude) coordinates of the starting point.
        end_coords (tuple): The (latitude, longitude) coordinates of the ending point.
        mode (str): The mode of transportation to use. Options are "car", "bike", and "foot". Default is "car".
        api_key (str): Your API key for the OpenRouteService API. If not provided, the free version of the API will be used.

    Returns:
        route_data (dict): A dictionary containing the route data, including coordinates and travel time.
    """
    # Set up API endpoint URL and parameters
    api_url = "https://api.openrouteservice.org/v2/directions/{}/geojson".format(mode)
    params = {
        "start": "{},{}".format(start_coords[1], start_coords[0]), # swap lat/long order
        "end": "{},{}".format(end_coords[1], end_coords[0]), # swap lat/long order
        "api_key": api_key
    }

    # Send GET request to API endpoint
    response = requests.get(api_url, params=params)

    # Parse JSON response and extract route data
    data = json.loads(response.content)
    route_data = {
        "coordinates": data["features"][0]["geometry"]["coordinates"],
        "travel_time": data["features"][0]["properties"]["segments"][0]["duration"]
    }

    return route_data

def predict_safety(route):
    # Load the pre-trained models for crime, weather, and road safety
    crime_model = load_model('crime_model.h5')
    weather_model = load_model('weather_model.h5')
    road_model = load_model('road_model.h5')

    # Load the route data and engineer features
    route_data = load_route_data(route)
    route_features = engineer_features(route_data)

    # Make predictions using the trained models
    crime_prediction = crime_model.predict(route_features)
    weather_prediction = weather_model.predict(route_features)
    road_prediction = road_model.predict(route_features)

    # Compute the final safety score using location-wise weightages
    safety_score = (0.4 * crime_prediction) + (0.3 * weather_prediction) + (0.3 * road_prediction)

    return safety_score


if __name__ == '__main__':
    model = load_model()
    route_data = # code to get the route data from user input
    risk_factor = predict_risk(route_data)
    print(f"The predicted risk factor of this route is {risk_factor}")
