import pandas as pd

# Read the crime dataset
crime_data = pd.read_csv('crime_data.csv')

# Calculate the danger score for each crime type
danger_score = {'theft': 1, 'burglary': 2, 'arson': 5, 'vandalism': 3, 'murder': 10, 'assault': 8, 'sexual_assault': 9, 'speeding': 2, 'reckless_driving': 3, 'carjacking': 6}

# Calculate the danger index for each location
danger_index = {}
for index, row in crime_data.iterrows():
    location = (row['latitude'], row['longitude'])
    crime_type = row['crime_type']
    if location not in danger_index:
        danger_index[location] = 0
    danger_index[location] += danger_score[crime_type]

# Print the danger index for each location
for location, index in danger_index.items():
    print(f"Location: {location}, Danger Index: {index}")
