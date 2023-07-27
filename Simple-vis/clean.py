import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)
num_rows = 100
dates = pd.date_range(start='2023-01-01', periods=num_rows)
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack']
ages = np.random.randint(20, 60, num_rows).astype(float)
weights = np.random.randint(50, 100, num_rows).astype(float)
lengths = np.random.randint(150, 200, num_rows).astype(float)

# Introduce missing values
missing_idx = np.random.choice(num_rows, 10, replace=False)
ages[missing_idx] = np.nan
weights[missing_idx] = np.nan
lengths[missing_idx] = np.nan

# Create DataFrame
data = {
    'Date': dates,
    'Name': np.random.choice(names, num_rows),
    'Age': ages,
    'Weight': weights,
    'Length': lengths
}
df = pd.DataFrame(data)

# Interpolate missing values
df.interpolate(inplace=True)

# Index by Day
df.set_index('Date', inplace=True)

# Save to a .csv file
df.to_csv('cleaned_random_data.csv')
