import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data for 3 districts
districts = ['District A', 'District B', 'District C']
months = pd.date_range('2023-01-01', periods=12, freq='MS')

# Generate random data for each district separately
square_feet_data = {
    'District': np.repeat(districts, 12),
    'Date': np.tile(months, 3),
    'Square Feet': np.random.randint(1000, 3000, size=36)
}

house_price_data = {
    'District': np.repeat(districts, 12),
    'Date': np.tile(months, 3),
    'House Price': np.random.randint(300000, 800000, size=36)
}

# Create DataFrames
square_feet_df = pd.DataFrame(square_feet_data)
house_price_df = pd.DataFrame(house_price_data)

# Output DataFrames to CSV files
square_feet_df.to_csv('square_feet_data.csv', index=False)
house_price_df.to_csv('house_price_data.csv', index=False)
