import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the aggregated data from the unemployement_aggregate.csv file
data = pd.read_csv('unemployement_aggregate.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("US Unemployment Data Visualization"),
    html.H3("Choose Visualization:"),
    dcc.Dropdown(
        id='visualization-type',
        options=[
            {'label': 'Box Visualization - Unemployment Rate by Race/Gender', 'value': 'box'},
            {'label': 'Histogram - Distribution of Unemployment Rate', 'value': 'histogram'},
            {'label': 'Scatterplot Matrix - Unemployment Rate by Race/Gender', 'value': 'scatter_matrix'}
        ],
        value='box'
    ),
    dcc.Graph(id='visualization-output')
])

# Callback to update the visualization based on the chosen option
@app.callback(
    Output('visualization-output', 'figure'),
    [Input('visualization-type', 'value')]
)
def update_visualization(selected_option):
    if selected_option == 'box':
        # Create a box plot for each race/gender
        fig = go.Figure()
        for race_gender in ['White', 'Black', 'Hispanic', 'Women', 'Men']:
            fig.add_trace(go.Box(y=data[race_gender], name=race_gender))
        fig.update_layout(title='Unemployment Rate by Race/Gender',
                          xaxis_title='Race/Gender',
                          yaxis_title='Unemployment Rate')
        return fig
    elif selected_option == 'histogram':
        # Create a histogram to visualize the distribution of the unemployment rate
        fig = go.Figure()
        for race_gender in ['White', 'Black', 'Hispanic', 'Women', 'Men']:
            fig.add_trace(go.Histogram(x=data[data[race_gender].notnull()][race_gender],
                                       name=race_gender,
                                       opacity=0.7))
        fig.update_layout(title='Distribution of Unemployment Rate by Race/Gender',
                          xaxis_title='Unemployment Rate',
                          yaxis_title='Frequency')
        return fig
    elif selected_option == 'scatter_matrix':
        # Create a Scatterplot Matrix to visualize the relationship between variables
        fig = px.scatter_matrix(data.drop(columns=['Date']), dimensions=['Unemployment_Rate', 'White', 'Black', 'Hispanic', 'Women', 'Men'],
                                color='Unemployment_Rate', color_continuous_scale='Viridis')
        fig.update_layout(title='Scatterplot Matrix - Unemployment Rate by Race/Gender',
                          height=800)
        return fig
    else:
        return go.Figure()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
