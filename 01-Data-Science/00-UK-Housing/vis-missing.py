import pandas as pd
import matplotlib.pyplot as plt

# Function to visualize missing data
def visualize_missing_data(df, title):
    missing_data = df.isnull()
    plt.figure(figsize=(10, 6))
    plt.title(f"Missing Data: {title}")
    plt.imshow(missing_data, cmap='viridis', aspect='auto')
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.xticks(range(len(df.columns)), df.columns, rotation=90)
    plt.yticks(range(len(df.index)), df.index)
    plt.colorbar(label="Missing Data (True: Missing, False: Available)")
    plt.tight_layout()
    plt.show()

# Load and clean housing_in_london_monthly_variables.csv
data_monthly = pd.read_csv('housing_in_london_monthly_variables.csv')

# Interpolate the missing data in 'houses_sold' using linear interpolation
data_monthly['houses_sold'] = data_monthly['houses_sold'].interpolate(method='linear')

# Fill missing data in 'no_of_crimes' with 0
if 'no_of_crimes' in data_monthly:
    data_monthly['no_of_crimes'].fillna(0, inplace=True)

# Format 'houses_sold' column to have only one decimal point
data_monthly['houses_sold'] = data_monthly['houses_sold'].round(1)

# Convert the 'date' column to datetime data type
data_monthly['Date'] = pd.to_datetime(data_monthly['date'])

# Sort the data in ascending order by 'Date' and alphabetically by 'area' within each date
data_monthly.sort_values(by=['Date', 'area'], inplace=True)

# Drop the 'Date' column as it is no longer needed for sorting
data_monthly.drop(columns=['Date'], inplace=True)

# Save the cleaned and sorted data to a new CSV file
data_monthly.to_csv('clean_housing_in_london_monthly_variables.csv', index=False)

# Visualize missing data in the monthly dataset
visualize_missing_data(data_monthly, "Housing in London Monthly Variables")

# Load and clean housing_in_london_yearly_variables.csv
data_yearly = pd.read_csv('housing_in_london_yearly_variables.csv')

# Fill missing data in 'no_of_crimes' with 0
if 'no_of_crimes' in data_yearly:
    data_yearly['no_of_crimes'].fillna(0, inplace=True)

# Convert the 'date' column to datetime data type
data_yearly['Date'] = pd.to_datetime(data_yearly['date'])

# Sort the data in ascending order by 'Date' and alphabetically by 'area' within each date
data_yearly.sort_values(by=['Date', 'area'], inplace=True)

# Drop the 'Date' column as it is no longer needed for sorting
data_yearly.drop(columns=['Date'], inplace=True)

# Save the cleaned and sorted data to a new CSV file
data_yearly.to_csv('clean_housing_in_london_yearly_variables.csv', index=False)

# Visualize missing data in the yearly dataset
visualize_missing_data(data_yearly, "Housing in London Yearly Variables")
