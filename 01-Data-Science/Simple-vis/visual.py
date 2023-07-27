import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('cleaned_random_data.csv', parse_dates=['Date'], index_col='Date')

# Line plot - Weekly average weight
weekly_weight_avg = df['Weight'].resample('W').mean()

plt.figure(figsize=(10, 6))
plt.plot(weekly_weight_avg.index, weekly_weight_avg.values, marker='o', linestyle='-', label='Weekly Average Weight')
for i, weight in enumerate(weekly_weight_avg):
    plt.text(weekly_weight_avg.index[i], weight, str(round(weight, 2)), ha='right', va='bottom')

plt.xlabel('Week')
plt.ylabel('Weight')
plt.title('Weekly Average Weight')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

# Scatter plot - Weekly average weight per person with name labels
plt.figure(figsize=(10, 6))
for name, data in df.groupby('Name'):
    weekly_avg = data['Weight'].resample('W').mean()
    plt.scatter(weekly_avg.index, weekly_avg, label=name)
    for i, weight in enumerate(weekly_avg):
        plt.text(weekly_avg.index[i], weight, str(round(weight, 2)), ha='right', va='bottom')

plt.xlabel('Week')
plt.ylabel('Average Weight')
plt.title('Weekly Average Weight per Person')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
