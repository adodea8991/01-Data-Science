import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Create the count plot
plt.figure(figsize=(8, 6))
ax = sns.countplot(x='Name', data=df, palette='pastel')

# Add labels to the count plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.xlabel('Name')
plt.ylabel('Count')
plt.title('Count Plot of Names')
plt.show()
