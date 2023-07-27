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

