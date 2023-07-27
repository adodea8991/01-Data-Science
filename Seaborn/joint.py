import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv('random_data_clean.csv', parse_dates=['Date'])

# Create the joint plot
sns.set(style="white")
g = sns.jointplot(x='Weight', y='Length', data=df, kind='scatter', color='skyblue')

# Calculate the correlation coefficient
corr_coef = df['Weight'].corr(df['Length'])

# Add label for correlation coefficient
g.ax_joint.annotate(f"Corr: {corr_coef:.2f}", xy=(0.6, 0.9), xycoords='axes fraction',
                    fontsize=12, color='black')

plt.show()
