import pandas as pd
import numpy as np
import random

# Define the latitude and longitude of the SRM KTR campus area
latitude = 12.8303
longitude = 80.0415

# Define the number of rows to generate
num_rows = 1000

# Define the range of values for latitude and longitude to use for generating random points in the area
latitude_range = 0.01
longitude_range = 0.01

# Define a list of street names
streets = ['SRM Main Rd', 'Potheri Main Rd', 'GST Rd', 'Thiruvanchery Rd', 'Chengalpattu-Thiruporur Rd']

# Define a list of crime types
crime_types = ['Robbery', 'Assault', 'Theft', 'Vandalism', 'Drug-related', 'Sexual assault']

# Define a list of months and years for which to generate crime data
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
years = ['2020', '2021', '2022']

# Generate random points within the defined area
lats = [random.uniform(latitude - latitude_range, latitude + latitude_range) for i in range(num_rows)]
longs = [random.uniform(longitude - longitude_range, longitude + longitude_range) for i in range(num_rows)]

# Create a dataframe with the generated points
df = pd.DataFrame({'latitude': lats, 'longitude': longs})

# Add columns for street name and crime type
df['street_name'] = [random.choice(streets) for i in range(num_rows)]
df['crime_type'] = [random.choice(crime_types) for i in range(num_rows)]

# Add columns for date and time of the crime
df['month'] = [random.choice(months) for i in range(num_rows)]
df['year'] = [random.choice(years) for i in range(num_rows)]
df['day'] = [random.randint(1, 28) for i in range(num_rows)]
df['hour'] = [random.randint(0, 23) for i in range(num_rows)]
df['minute'] = [random.randint(0, 59) for i in range(num_rows)]

# Save the dataframe as a CSV file
df.to_csv('crime_data.csv', index=False)
