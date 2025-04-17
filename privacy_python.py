import pandas as pd

# Define the data
data = {
    "Date": [
        "2023-01-02", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
        "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10"
    ],
    "CustomerID": ["C001", "C001", "C001", "C001", "C001", "C002", "C002", "C002", "C002", "C002"],
    "AccountBalance": [1500, 1500, 1500, 1500, 1500, 2060, 2000, 2000, 2000, 2000],
    "Close": [100, 102, 101, 105, 107, 106, 108, 110, 109, 111]
}

# Create a DataFrame
stock_prices = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
stock_prices['Date'] = pd.to_datetime(stock_prices['Date'], format='%Y-%m-%d')

# Display the DataFrame
print(stock_prices)