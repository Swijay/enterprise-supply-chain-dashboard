import pandas as pd
import numpy as np

def create_synthetic_data():
    """Generates 1 year of daily sales data for 3 products."""
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31")
    products = ['Product_A', 'Product_B', 'Product_C']
    
    data = []
    for product in products:
        base_sales = np.random.randint(20, 50)
        for date in dates:
            # Add weekend spikes (people buy more on weekends)
            is_weekend = 1 if date.dayofweek >= 5 else 0
            daily_sales = base_sales + (is_weekend * np.random.randint(15, 30)) + np.random.randint(-5, 10)
            
            data.append({
                'Date': date,
                'Product_ID': product,
                'Sales': max(0, daily_sales), # Ensure no negative sales
                'Current_Stock': np.random.randint(50, 300) # Random current stock for our dashboard
            })
            
    df = pd.DataFrame(data)
    # Save to the data folder
    import os
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv('data/raw/synthetic_sales.csv', index=False)
    print("✅ Synthetic data generated at data/raw/synthetic_sales.csv")

if __name__ == "__main__":
    create_synthetic_data()