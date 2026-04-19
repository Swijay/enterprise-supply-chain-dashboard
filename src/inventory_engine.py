import numpy as np

def calculate_inventory_metrics(historical_sales, forecasted_demand, lead_time_days=3):
    """Calculates Safety Stock and Reorder Point."""
    
    # 1. Calculate Standard Deviation of historical daily demand
    std_dev_demand = np.std(historical_sales)
    
    # 2. Safety Stock Formula: Z * StdDev * sqrt(Lead Time)
    # Z-score for 95% service level is approx 1.65
    z_score = 1.65
    safety_stock = int(z_score * std_dev_demand * np.sqrt(lead_time_days))
    
    # 3. Average Daily Forecast
    avg_daily_forecast = forecasted_demand / 7 
    
    # 4. Reorder Point Formula: (Lead Time * Avg Daily Forecast) + Safety Stock
    reorder_point = int((lead_time_days * avg_daily_forecast) + safety_stock)
    
    return safety_stock, reorder_point