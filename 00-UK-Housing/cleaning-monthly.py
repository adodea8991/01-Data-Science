import pandas as pd

# Load the dataset
data = pd.read_csv('housing_in_london_monthly_variables.csv')

# Interpolate the missing data in 'houses_sold' using linear interpolation
data['houses_sold'] = data['houses_sold'].interpolate(method='linear')

# Fill missing data in 'no_of_crimes' with 0
data['no_of_crimes'].fillna(0, inplace=True)

# Format 'houses_sold' column to have only one decimal point
data['houses_sold'] = data['houses_sold'].round(1)

# Convert the 'date' column to datetime data type
data['Date'] = pd.to_datetime(data['date'])

# Sort the data in ascending order by 'Date' and alphabetically by 'area' within each date
data.sort_values(by=['Date', 'area'], inplace=True)

# Drop the 'Date' column as it is no longer needed for sorting
data.drop(columns=['Date'], inplace=True)

# Save the cleaned and sorted data to a new CSV file
data.to_csv('clean_housing_in_london_monthly_variables.csv', index=False)
