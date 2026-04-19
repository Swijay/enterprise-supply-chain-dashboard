import pandas as pd
import os

def download_real_dataset():
    print("⏳ Downloading Global Superstore Dataset from the internet...")
    
    # Direct URL to a public GitHub repository hosting the real dataset
    url = 'https://raw.githubusercontent.com/yannie28/Global-Superstore/master/Global_Superstore(CSV).csv'
    
    # Pandas can read data directly from a URL! (using latin1 encoding for special characters)
    df = pd.read_csv(url, encoding='latin1')
    
    # Ensure the data folder exists
    os.makedirs('data/raw', exist_ok=True)
    
    # Save it locally so you don't have to download it every time
    filepath = 'data/raw/real_superstore_data.csv'
    df.to_csv(filepath, index=False)
    
    print(f"✅ SUCCESS! Downloaded {len(df)} rows of REAL retail data.")
    print(f"📁 Saved to: {filepath}")
    
    # Show a tiny preview of the columns
    print("\nColumns in this dataset:")
    print(df.columns.tolist()[:10], "...")

if __name__ == "__main__":
    download_real_dataset()