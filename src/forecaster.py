import xgboost as xgb
import pandas as pd

def train_and_forecast(df, product_id, forecast_days=7):
    """Trains an XGBoost model for a specific product and predicts future demand."""
    # Filter for the selected product
    product_df = df[df['Product_ID'] == product_id].copy()
    
    # Define features (X) and target (y)
    features = ['DayOfWeek', 'Month', 'Is_Weekend', 'Lag_7', 'Rolling_Mean_7']
    X = product_df[features]
    y = product_df['Sales']
    
    # Train the XGBoost Regressor (simplified for beginner execution)
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)
    model.fit(X, y)
    
    # Create future dataframe for predictions
    last_date = product_df['Date'].max()
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=forecast_days)
    
    # For a beginner project, we use the last known lag/rolling stats to predict the immediate future
    last_lag_7 = product_df['Lag_7'].iloc[-1]
    last_rolling = product_df['Rolling_Mean_7'].iloc[-1]
    
    future_data = []
    for date in future_dates:
        future_data.append({
            'DayOfWeek': date.dayofweek,
            'Month': date.month,
            'Is_Weekend': 1 if date.dayofweek >= 5 else 0,
            'Lag_7': last_lag_7, 
            'Rolling_Mean_7': last_rolling
        })
        
    future_df = pd.DataFrame(future_data)
    predictions = model.predict(future_df)
    
    # Return total predicted demand for the forecast window
    return sum(predictions), predictions, future_dates