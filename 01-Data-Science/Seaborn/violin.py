import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Create the violin plot
plt.figure(figsize=(10, 6))
ax = sns.violinplot(data=df, x='Name', y='Weight')

plt.title('Violin Plot of Weight by Name')
plt.xlabel('Name')
plt.ylabel('Weight')

# Add labels to the violins
for line in ax.collections:
    x = line.get_paths()[0].vertices[:, 0]
    y = line.get_paths()[0].vertices[:, 1]
    if len(y) > 0:  # Skip empty violins
        x_pos = x.mean()  # Adjust the horizontal position of the label
        y_pos = y.max() + 1  # Adjust the vertical position of the label
        ax.text(x_pos, y_pos, f'{y.max():.0f}', ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()
