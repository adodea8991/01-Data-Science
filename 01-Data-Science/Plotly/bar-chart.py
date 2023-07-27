import pandas as pd
import plotly.graph_objects as go

# Read the data from the CSV file
df = pd.read_csv('house_price_data.csv')

# Calculate the average house price for each district
avg_house_price = df.groupby('District')['House Price'].mean().reset_index()

# Create a Bar chart object
fig_bar = go.Figure(data=[go.Bar(x=avg_house_price['District'], y=avg_house_price['House Price'])])

# Update the layout for better readability
fig_bar.update_layout(title='Average House Price by District',
                      xaxis_title='District',
                      yaxis_title='Average House Price')

# Show the interactive bar chart
fig_bar.show()
