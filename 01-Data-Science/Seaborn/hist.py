import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Create the histogram
plt.figure(figsize=(10, 6))
ax = sns.histplot(data=df, x='Age', kde=True)

plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Add labels to the bars
for p in ax.patches:
    height = p.get_height()
    if height > 0:  # Skip zero values
        ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom', fontsize=10)

plt.show()
