import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Create the pair plot
sns.set(style="ticks")
g = sns.pairplot(df, hue='Name', diag_kind='kde', markers='o')

# Calculate the correlation coefficients
corr_matrix = df.drop(columns=['Date', 'Name']).corr()

# Add labels for correlation coefficients
for i, (row_name, corr_values) in enumerate(corr_matrix.iterrows()):
    for j, corr_value in enumerate(corr_values):
        if i < j:
            x = g.axes[j, i].get_xlim()[0] + 0.5
            y = g.axes[j, i].get_ylim()[1] - 0.1
            g.axes[j, i].text(x, y, f"{corr_value:.2f}", ha='left', va='top', fontsize=10, color='black')

plt.show()
