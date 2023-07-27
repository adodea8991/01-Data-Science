# Project: London Housing Data Analysis

This repository contains Python scripts to analyze and clean London housing data from two different datasets: `housing_in_london_monthly_variables.csv` and `housing_in_london_yearly_variables.csv`.

## Overview

London housing data is essential for understanding the real estate market in the city. However, the datasets may contain missing data and require cleaning before performing meaningful analysis. In this project, we will perform the following steps:

1. Visualize missing data in both `housing_in_london_monthly_variables.csv` and `housing_in_london_yearly_variables.csv`.
2. Clean the data using `cleaning-monthly.py` to generate `clean_housing_in_london_monthly_variables.csv`.
3. Aggregate the data using `aggregate.py` to combine monthly and yearly variables for further analysis.
4. Create visualizations to gain insights from the data.

## Dataset

The two main datasets used in this project are:
- `housing_in_london_monthly_variables.csv`: Contains monthly housing variables for different London boroughs.
- `housing_in_london_yearly_variables.csv`: Contains yearly housing variables for different London boroughs.

## Code Files

1. `vis-missing.py`: This script visualizes missing data in the two datasets.
2. `cleaning-monthly.py`: This script cleans the `housing_in_london_monthly_variables.csv` file and generates `clean_housing_in_london_monthly_variables.csv`.
3. `aggregate.py`: This script combines the monthly and yearly variables and creates visualizations.

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/london-housing-analysis.git
cd london-housing-analysis
```

2. Visualize missing data:

```bash
python vis-missing.py
```

These will be the resulting views:


![Monthly missing data](https://github.com/adodea8991/01-Data-Science/blob/main/00-UK-Housing/Missing-monthly.png)


![Yearly missing data](https://github.com/adodea8991/01-Data-Science/blob/main/00-UK-Housing/Missing-yearly.png)

3. Clean the monthly data:

```bash
python cleaning-monthly.py
```

4. Aggregate the data and create visualizations:

```bash
python aggregate.py
```

## Data Cleaning

The `cleaning-monthly.py` script performs data cleaning on the `housing_in_london_monthly_variables.csv` dataset by handling missing values and converting data to appropriate formats.

## Aggregation

The `aggregate.py` script combines the monthly and yearly data into a single dataset for further analysis.

## Visualization

The `aggregate.py` script generates various visualizations, such as line plots, bar charts, and scatter plots, to provide insights into the London housing market.

## Conclusion

This project aims to provide a comprehensive analysis of London housing data, enabling us to better understand the trends and patterns in the real estate market. Feel free to explore the cleaned datasets and the visualizations to gain valuable insights.

Please let me know if you need any further assistance or have any questions. Happy analyzing!






# Project: US Unemployment Data Analysis

This repository contains Python scripts to analyze and visualize US unemployment data from two different datasets: `unemployment_data_us_state.csv` and `unemployment_data_us.csv`.

## Overview

Unemployment data is crucial for understanding the job market and economic conditions in different regions of the United States. In this project, we will perform the following steps:

1. Visualize regional unemployment data per state using `unemployment.py`.
2. Aggregate the data from `unemployment_data_us_state.csv` and `unemployment_data_us.csv` into a single dataset using `aggregate_data.py` to generate `unemployment_aggregate.csv`.
3. Create visualizations to gain insights into the US unemployment trends using `vis_unemployment.py`.

## Datasets

The two main datasets used in this project are:
- `unemployment_data_us_state.csv`: Contains unemployment data per state over the years.
- `unemployment_data_us.csv`: Contains overall US unemployment data over the years.

## Code Files

1. `unemployment.py`: This script visualizes regional unemployment data per state, creating box plots and linear plots for each state over the years.
2. `aggregate_data.py`: This script combines the data from `unemployment_data_us_state.csv` and `unemployment_data_us.csv` into a single dataset, generating `unemployment_aggregate.csv`.
3. `vis_unemployment.py`: This script generates three visualizations for US unemployment data: a box plot, a histogram, and a scatter plot.

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/us-unemployment-analysis.git
cd us-unemployment-analysis
```

2. Visualize regional unemployment data per state:

```bash
python unemployment.py
```

![Box plot per state](https://github.com/adodea8991/01-Data-Science/blob/main/00-US-Unemployement/F1-Distribution-per-State.png)
![Linear plot per state](https://github.com/adodea8991/01-Data-Science/blob/main/00-US-Unemployement/F2-Rates-per-Day.png)


3. Aggregate the data:

```bash
python aggregate_data.py
```

4. Create visualizations:

```bash
python vis_unemployment.py
```

![Box plot](https://github.com/adodea8991/01-Data-Science/blob/main/00-US-Unemployement/box-plot.png)
![Histogram](https://github.com/adodea8991/01-Data-Science/blob/main/00-US-Unemployement/histogram.png)
![Scatter plot](https://github.com/adodea8991/01-Data-Science/blob/main/00-US-Unemployement/scatter-plot.png)


## Regional Unemployment Data Visualization

The `unemployment.py` script creates visualizations to show regional unemployment data per state. It generates box plots and linear plots for each state, providing insights into the unemployment trends over the years.

## Data Aggregation

The `aggregate_data.py` script combines the data from `unemployment_data_us_state.csv` and `unemployment_data_us.csv` into a single dataset, `unemployment_aggregate.csv`, for further analysis.

## Visualization

The `vis_unemployment.py` script generates three visualizations for US unemployment data:

1. Box Plot: The box plot provides a graphical representation of the distribution of unemployment rates in the United States, helping to identify outliers and variations in different regions.
2. Histogram: The histogram displays the frequency distribution of unemployment rates, enabling us to understand the data's overall distribution.
3. Scatter Plot: The scatter plot shows the relationship between unemployment rates and other variables, such as GDP or population, to explore potential correlations.

## Conclusion

This project aims to provide valuable insights into the US unemployment data, enabling a better understanding of regional employment trends and economic conditions. Feel free to explore the visualizations and the aggregated dataset to gain further insights.




# Interactive Housing Data Dashboard

Welcome to the Interactive Housing Data Dashboard! This dashboard allows you to explore and analyze housing data from `house_price_data.csv`. It provides three interactive visualizations:

1. Line Chart: This chart displays the trend of house prices per district over time. You can hover over data points to see detailed information.

2. Scatter Plot: The scatter plot shows the relationship between district and house prices. Hovering over data points will reveal specific district and price details.

3. Bar Chart: This chart presents a comparison of house prices among different districts. Hover over each bar to view the exact price for that district.

## How to Run the Dashboard

1. Make sure you have Python installed on your system.

2. Install the required libraries by running the following command in your terminal:

```bash
pip install pandas plotly dash
```

3. Download or clone this repository to your local machine.

4. Navigate to the directory containing `dashboard.py` and the `house_price_data.csv` file.

5. To launch the dashboard, execute the following command:

```bash
python dashboard.py
```

![Dashboard view](https://github.com/adodea8991/01-Data-Science/blob/main/00-Dashboard/Screenshot%202023-07-27%20at%2023.34.15.png)


6. The program will start a local server, and you can access the dashboard by opening your web browser and visiting the provided URL (usually `http://127.0.0.1:8050/`).

7. The dashboard provides buttons on the left to activate/deactivate different visualizations. Use the hover functionality to gain insights into specific data points.

## Tips for Interacting with the Dashboard

- Toggle the buttons on the left to switch between line chart, scatter plot, and bar chart.

- Hover over data points in each visualization to view additional information.

- Use the interactive features to explore the trends and relationships between house prices and districts.

Feel free to experiment with different visualizations and gain valuable insights into the housing data. If you encounter any issues or have questions, please don't hesitate to reach out. Enjoy exploring the Interactive Housing Data Dashboard!