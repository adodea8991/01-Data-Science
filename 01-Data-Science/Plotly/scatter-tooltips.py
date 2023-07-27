import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

# Load the data from the CSV file
df = pd.read_csv('house_price_data.csv')

# Create a Scatter graph object with tooltips
trace = go.Scatter(x=df['Date'], y=df['House Price'], mode='markers', text=df['District'],
                   hovertemplate='<b>District:</b> %{text}<br><b>Date:</b> %{x}<br><b>House Price:</b> %{y}')

# Create layout
layout = go.Layout(title='Scatter Plot with Tooltips', xaxis_title='Date', yaxis_title='House Price')

# Create figure and plot
fig = go.Figure(data=[trace], layout=layout)

# Save the plot as an HTML file and open it in your browser
pyo.plot(fig, filename='scatter_plot.html')
