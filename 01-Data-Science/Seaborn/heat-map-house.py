import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
data = pd.read_csv('house_prices_dataset.csv', parse_dates=['Date'])

# Calculate the correlation matrix
correlation_matrix = data[['SquareFeet', 'HousePrice']].corr()

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap - Square Feet vs House Price')
plt.show()
