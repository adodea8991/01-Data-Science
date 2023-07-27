import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Read the data from the CSV file
df = pd.read_csv('house_price_data.csv')

# Create a Line chart with hover
fig_line = go.Figure(data=[go.Scatter(x=df['Date'], y=df['House Price'], mode='lines+markers', hoverinfo='text',
                                     text=df['House Price'])])
fig_line.update_layout(title='House Price Over Time',
                       xaxis_title='Date',
                       yaxis_title='House Price')

# Create a Scatter plot with tooltips
fig_scatter = go.Figure(data=[go.Scatter(x=df['Date'], y=df['House Price'], mode='markers', hoverinfo='text',
                                        text=df['House Price'])])
fig_scatter.update_layout(title='House Price vs. Date',
                          xaxis_title='Date',
                          yaxis_title='House Price')

# Create a Bar chart
fig_bar = go.Figure(data=[go.Bar(x=df['District'], y=df['House Price'])])
fig_bar.update_layout(title='House Price by District',
                      xaxis_title='District',
                      yaxis_title='House Price')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1("Interactive Dashboard"),

    # Buttons to show/hide graphs
    dcc.Checklist(
        id='graph-toggle',
        options=[
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Bar Chart', 'value': 'bar'}
        ],
        value=['line', 'scatter', 'bar']
    ),

    # Line chart with hover
    dcc.Graph(id='line-chart', figure=fig_line, style={'display': 'inline-block', 'width': '33%'}),

    # Scatter plot with tooltips
    dcc.Graph(id='scatter-plot', figure=fig_scatter, style={'display': 'inline-block', 'width': '33%'}),

    # Bar chart
    dcc.Graph(id='bar-chart', figure=fig_bar, style={'display': 'inline-block', 'width': '33%'})
])

# Callback to toggle visibility of graphs based on button selection
@app.callback(
    Output('line-chart', 'style'),
    Output('scatter-plot', 'style'),
    Output('bar-chart', 'style'),
    Input('graph-toggle', 'value')
)
def toggle_graphs(selected_graphs):
    style = {'display': 'none'}
    line_style, scatter_style, bar_style = style, style, style

    if 'line' in selected_graphs:
        line_style = {'display': 'inline-block', 'width': '33%'}
    if 'scatter' in selected_graphs:
        scatter_style = {'display': 'inline-block', 'width': '33%'}
    if 'bar' in selected_graphs:
        bar_style = {'display': 'inline-block', 'width': '33%'}

    return line_style, scatter_style, bar_style

# Run the Dash app on host '0.0.0.0' to make it accessible from other devices on the same network
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
