import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

# Load the data from unemployment_data_us_state.csv
data = pd.read_csv('unemployment_data_us_state.csv')

# Convert 'Date' column to datetime type with format '%b-%Y'
data['Date'] = pd.to_datetime(data['Date'], format='%b-%Y')

# Sort the data by 'State' and 'Date' columns
data = data.sort_values(by=['State', 'Date'])

# Interpolate missing 'Unemployment_Rate' values for each state
data['Unemployment_Rate'] = data.groupby('State')['Unemployment_Rate'].transform(lambda x: x.interpolate())

# Create a box plot to show the distribution of unemployment rates per state
plt.figure(figsize=(12, 8))
sns.boxplot(x='State', y='Unemployment_Rate', data=data)
plt.xlabel('State')
plt.ylabel('Unemployment Rate')
plt.title('Distribution of Unemployment Rates per State')
plt.xticks(rotation=90)

# Add hover function to display relevant information
ax = plt.gca()
for box in ax.artists:
    box.set_picker(True)
plt.tight_layout()
plt.show()

# Create a pivot table to calculate the average unemployment rates per day per state
pivot_table = data.pivot_table(index='Date', columns='State', values='Unemployment_Rate', aggfunc='mean').reset_index()

# Create a line plot to show the unemployment rate per day for each individual state
fig = make_subplots(rows=1, cols=1, shared_xaxes=False, shared_yaxes=True)

for state in pivot_table.columns[1:]:
    fig.add_trace(go.Scatter(x=pivot_table['Date'], y=pivot_table[state], mode='lines', name=state))

fig.update_layout(title_text="Unemployment Rates per Day",
                  xaxis_title="Date",
                  yaxis_title="Unemployment Rate",
                  legend_title="State",
                  showlegend=True)

fig.show()