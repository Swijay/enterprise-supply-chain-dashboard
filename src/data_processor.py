import pandas as pd

def load_and_engineer_features(filepath):
    """Loads raw data and creates machine learning features."""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by=['Product_ID', 'Date'])
    
    # 1. Date Features
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month
    df['Is_Weekend'] = df['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)
    
    # 2. Lag Features (What were the sales 7 days ago?)
    # We group by product so we don't mix Product A's history with Product B
    df['Lag_7'] = df.groupby('Product_ID')['Sales'].shift(7)
    
    # 3. Rolling Average (Smooth out the noise)
    df['Rolling_Mean_7'] = df.groupby('Product_ID')['Sales'].transform(lambda x: x.rolling(window=7).mean())
    
    # Drop rows with NaN values created by lag/rolling features
    df = df.dropna()
    
    return df