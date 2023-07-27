import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Create the box plot
plt.figure(figsize=(10, 6))
ax = sns.boxplot(data=df, x='Name', y='Weight')

plt.title('Box Plot of Weight by Name')
plt.xlabel('Name')
plt.ylabel('Weight')

# Add labels to the boxes
for line in ax.get_lines():
    y = line.get_ydata()
    x = line.get_xdata()
    if len(y) > 0:  # Skip empty boxes
        y_pos = y.max() + 1  # Adjust the vertical position of the label
        ax.text(x[0], y_pos, f'{y.max():.0f}', ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()
