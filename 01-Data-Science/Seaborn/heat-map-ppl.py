import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Select only the numeric columns for correlation computation
numeric_columns = df.select_dtypes(include=['int64', 'float64'])

# Compute the correlation matrix
correlation_matrix = numeric_columns.corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title('Correlation Heatmap')
plt.show()
