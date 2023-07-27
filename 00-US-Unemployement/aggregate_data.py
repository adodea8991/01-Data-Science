import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the two CSV files
data1 = pd.read_csv('unemployment_data_us_state.csv')
data2 = pd.read_csv('unemployment_data_us.csv')

# Convert 'Date' column to datetime type with format '%b-%Y' in data1
data1['Date'] = pd.to_datetime(data1['Date'], format='%b-%Y')

# Combine 'Year' and 'Month' columns into a single 'Date' column in data2
data2['Date'] = pd.to_datetime(data2['Year'].astype(str) + '-' + data2['Month'], format='%Y-%b')

# Drop 'Year' and 'Month' columns from data2 as we now have 'Date'
data2 = data2.drop(columns=['Year', 'Month'])

# Calculate the mean of unemployment rate per month from data1
mean_unemployment_rate = data1.groupby('Date')['Unemployment_Rate'].mean().reset_index()

# Merge data2 with the mean_unemployment_rate on 'Date' using an outer join
combined_data = pd.merge(data2, mean_unemployment_rate, on='Date', how='outer')

# Interpolate missing 'Unemployment_Rate' values using linear interpolation
combined_data['Unemployment_Rate'] = combined_data['Unemployment_Rate'].interpolate(method='linear')

# Interpolate missing data about race and gender
combined_data['Primary_School'] = combined_data['Primary_School'].interpolate(method='linear')
combined_data['High_School'] = combined_data['High_School'].interpolate(method='linear')
combined_data['Associates_Degree'] = combined_data['Associates_Degree'].interpolate(method='linear')
combined_data['Professional_Degree'] = combined_data['Professional_Degree'].interpolate(method='linear')
combined_data['White'] = combined_data['White'].interpolate(method='linear')
combined_data['Black'] = combined_data['Black'].interpolate(method='linear')
combined_data['Asian'] = combined_data['Asian'].interpolate(method='linear')
combined_data['Hispanic'] = combined_data['Hispanic'].interpolate(method='linear')
combined_data['Men'] = combined_data['Men'].interpolate(method='linear')
combined_data['Women'] = combined_data['Women'].interpolate(method='linear')

# Clean the data to ensure all existing values are float with 2 decimal points
columns_to_clean = ['Unemployment_Rate', 'Primary_School', 'High_School', 'Associates_Degree',
                    'Professional_Degree', 'White', 'Black', 'Asian', 'Hispanic', 'Men', 'Women']

for column in columns_to_clean:
    combined_data[column] = combined_data[column].round(2)

# Reorder the columns with 'Date' as the first column
combined_data = combined_data[['Date'] + [col for col in combined_data.columns if col != 'Date']]

# Save the combined and cleaned data to unemployement_aggregate.csv
combined_data.to_csv('unemployement_aggregate.csv', index=False)

# Simple plot to visualize the data
plt.figure(figsize=(12, 6))

plt.plot(combined_data['Date'], combined_data['Unemployment_Rate'], marker='o', markersize=5, label='Unemployment Rate')
plt.plot(combined_data['Date'], combined_data['White'], marker='o', markersize=5, label='White')
plt.plot(combined_data['Date'], combined_data['Black'], marker='o', markersize=5, label='Black')
plt.plot(combined_data['Date'], combined_data['Asian'], marker='o', markersize=5, label='Asian')
plt.plot(combined_data['Date'], combined_data['Hispanic'], marker='o', markersize=5, label='Hispanic')
plt.plot(combined_data['Date'], combined_data['Men'], marker='o', markersize=5, label='Men')
plt.plot(combined_data['Date'], combined_data['Women'], marker='o', markersize=5, label='Women')

plt.xlabel('Date')
plt.ylabel('Percentage')
plt.title('Unemployment Rate and Demographics Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Add data labels to the plot
for column in columns_to_clean[1:]:
    for i, row in combined_data.iterrows():
        plt.annotate(f"{row[column]}", (row['Date'], row[column]), textcoords="offset points", xytext=(0, 5), ha='center')

plt.show()
