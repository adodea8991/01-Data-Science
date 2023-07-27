import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Scatter plot with labels
sns.scatterplot(x='Age', y='Weight', data=df, hue='Name')

# Add labels to each point
for _, row in df.iterrows():
    plt.text(row['Age'], row['Weight'], f"({row['Age']}, {row['Weight']})", fontsize=8, ha='right', va='bottom')

plt.title('Scatter Plot with Labels')
plt.show()
