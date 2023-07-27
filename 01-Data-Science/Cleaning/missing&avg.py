import pandas as pd
import numpy as np

# Load data from CSV file
df = pd.read_csv('random_data_with_missing.csv', parse_dates=['Date'])

# Convert 'Date' column to datetime and set it as the index
df.set_index('Date', inplace=True)

# Interpolate missing values in the 'Weight' column
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce').interpolate()

# Group by 'Name' and weekly frequency, and calculate the mean weight per person
weekly_weight_avg_per_person = df.groupby(['Name', pd.Grouper(freq='W')])['Weight'].mean()

# Reset index to get 'Name' and 'Date' back as columns
weekly_weight_avg_per_person = weekly_weight_avg_per_person.reset_index()

# Save the result into another CSV file
weekly_weight_avg_per_person.to_csv('weekly_weight_average_per_person.csv', index=False)
