import pandas as pd
import numpy as np

# generate random geocodes
latitude = np.random.uniform(low=12.840, high=12.860, size=(1000,))
longitude = np.random.uniform(low=80.000, high=80.020, size=(1000,))

# generate random crime data
crime_types = ['sexual harassment', 'assault', 'theft', 'vandalism']
crime_density = np.random.randint(1, 6, size=(1000,))
time_of_day = np.random.choice(['day', 'night'], size=(1000,))
crime_data = pd.DataFrame({'latitude': latitude,
                           'longitude': longitude,
                           'crime_type': np.random.choice(crime_types, size=(1000,)),
                           'crime_density': crime_density,
                           'time_of_day': time_of_day})

# one-hot encode the categorical variables
crime_data = pd.get_dummies(crime_data, columns=['crime_type', 'time_of_day'])

# save the dataset to a csv file
crime_data.to_csv('crime_data.csv', index=False)
