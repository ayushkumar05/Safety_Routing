import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from geopy.distance import distance

# Load the crime data
crime_data = pd.read_csv('crime_data.csv')

# Clean the data
crime_data = crime_data.dropna()
crime_data['coordinates'] = list(zip(crime_data['latitude'], crime_data['longitude']))
crime_data['time_of_day'] = pd.to_datetime(crime_data['date']).dt.hour
crime_data['day_of_week'] = pd.to_datetime(crime_data['date']).dt.day_name()
crime_data['day_of_week'] = pd.get_dummies(crime_data['day_of_week'])

# Load the road network data
road_network = pd.read_csv('road_network.csv')

# Define a function to compute the distance between a point and a road segment
def distance_to_segment(point, segment):
    start_point = segment[['start_latitude', 'start_longitude']].values
    end_point = segment[['end_latitude', 'end_longitude']].values
    return distance(start_point, point).km + distance(end_point, point).km

# Define a function to compute the safety score of a road segment
def compute_safety_score(segment, crime_data):
    crime_data['distance_to_segment'] = crime_data['coordinates'].apply(lambda x: distance_to_segment(x, segment))
    crime_data = crime_data[crime_data['distance_to_segment'] < 0.1] # consider only crimes within 100 meters of the road segment
    if len(crime_data) == 0:
        return 1.0
    else:
        crime_rate = len(crime_data[crime_data['crime_type'] == 'violent']) / len(crime_data)
        return 1.0 - crime_rate

# Compute the safety scores of all road segments
road_network['safety_score'] = road_network.apply(lambda x: compute_safety_score(x, crime_data), axis=1)

# Train a machine learning model to predict the safety of a road segment
X = road_network.drop(['start_point', 'end_point', 'safety_score'], axis=1)
y = road_network['safety_score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred)
print(f'AUC: {auc}')

# Save the machine learning model
joblib.dump(clf, 'crime_model.pkl')
