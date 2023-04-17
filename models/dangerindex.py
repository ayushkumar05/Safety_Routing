import pandas as pd

def danger_index(lat, long, crime_type, pop_density, year, month, date, hours, minutes, seconds):
    # Load crime dataset
    df = pd.read_csv("crime_data.csv")
    
    # Filter data based on parameters
    df = df[(df['latitude'] == lat) & (df['longitude'] == long) & (df['crime_type'] == crime_type) & 
            (df['pop_density'] == pop_density) & (df['year'] == year) & (df['month'] == month) & 
            (df['date'] == date) & (df['hours'] == hours) & (df['minutes'] == minutes) & 
            (df['seconds'] == seconds)]
    
    # Calculate danger index
    danger_index = df.shape[0] / pop_density
    
    return danger_index
