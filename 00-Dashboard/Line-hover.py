import pandas as pd
import plotly.graph_objs as go

# Load the data from the CSV file
df = pd.read_csv('house_price_data.csv', parse_dates=['Date'])

# Create the line chart using Plotly
fig = go.Figure()

# Add trace for each district
for district in df['District'].unique():
    df_district = df[df['District'] == district]
    fig.add_trace(go.Scatter(x=df_district['Date'], y=df_district['House Price'],
                             mode='lines+markers', name=district))

# Update the layout
fig.update_layout(title='House Price Trend by District',
                  xaxis_title='Date',
                  yaxis_title='House Price',
                  hovermode='x')

# Show the interactive line chart
fig.show()
