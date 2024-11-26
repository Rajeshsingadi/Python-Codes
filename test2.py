# Import necessary libraries
import pandas as pd
import numpy as np

# Define the function to calculate Money-Weighted Return (MWR)
def calculate_money_weighted_return(df):
    """
    This function calculates the Money-Weighted Return (MWR) using the numpy.irr() function.
    The portfolio cash flows include both the portfolio value changes and any external cash flows.
    """

    # Step 1: Create a list of cash flows
    # The first value in cash_flows is the initial portfolio value (negative because it's an outflow)
    # All other values include any changes in the portfolio value and any cash inflows or outflows
    cash_flows = df['cash_flow'].tolist()
    
    # Step 2: Append the final portfolio value (as a positive inflow)
    # This simulates the portfolio being liquidated at the end
    cash_flows.append(df['portfolio_value'].iloc[-1])
    
    # Step 3: Use numpy.irr() to calculate the internal rate of return (IRR), which is the MWR
    money_weighted_return = np.irr(cash_flows)
    
    # Step 4: Return the MWR
    return money_weighted_return

# Example: Create a DataFrame with portfolio values, cash flows over time
data = {
    'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'portfolio_value': [1000, 1100, 1050, 1150, 1200],  # Portfolio values at different dates
    'cash_flow': [-1000, 100, -50, 100, 0]  # Cash inflows (positive) and outflows (negative)
}

# Step 5: Create a Pandas DataFrame from the sample data
df = pd.DataFrame(data)

# Step 6: Call the function to calculate MWR and print the result
money_weighted_return = calculate_money_weighted_return(df)
print("Money-Weighted Return (MWR):", money_weighted_return)
