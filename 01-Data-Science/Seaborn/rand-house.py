import pandas as pd
import numpy as np

# Generate random data for the dataset
np.random.seed(42)

# Dates for one year timeline
dates = pd.date_range('2023-01-01', periods=365, freq='D')

# Square feet size data
square_feet_a = np.random.randint(1000, 3000, size=len(dates))
square_feet_b = np.random.randint(1000, 3000, size=len(dates))
square_feet_c = np.random.randint(1000, 3000, size=len(dates))

# House prices for three districts
house_prices_a = np.random.randint(300000, 700000, size=len(dates))
house_prices_b = np.random.randint(400000, 800000, size=len(dates))
house_prices_c = np.random.randint(500000, 900000, size=len(dates))

# Create a DataFrame
data = pd.DataFrame({
    'Date': dates.tolist() + dates.tolist() + dates.tolist(),
    'District': ['District A'] * len(dates) + ['District B'] * len(dates) + ['District C'] * len(dates),
    'SquareFeet': np.concatenate([square_feet_a, square_feet_b, square_feet_c]),
    'HousePrice': np.concatenate([house_prices_a, house_prices_b, house_prices_c])
})

# Save the DataFrame to a CSV file
data.to_csv('house_prices_dataset.csv', index=False)
