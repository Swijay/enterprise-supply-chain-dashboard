import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import timedelta

# -------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -------------------------------------------------------------------------
st.set_page_config(page_title="Global Retail Supply Chain", page_icon="🌍", layout="wide")

st.markdown("""
    <style>
    .metric-card { background-color: #1E1E1E; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #333; }
    .metric-value { font-size: 2rem; font-weight: bold; color: #4CAF50; }
    .metric-label { font-size: 1rem; color: #888; }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Global Superstore Inventory Optimization")
st.markdown("Live dashboard running on real-world retail data.")

# -------------------------------------------------------------------------
# 2. DATA LOADING & TRANSLATING (The Fix!)
# -------------------------------------------------------------------------
@st.cache_data
def load_data():
    try:
        # Load the real dataset
        df = pd.read_csv('data/raw/real_superstore_data.csv', encoding='latin1')
        
        # TRANSLATOR: Map Global Superstore columns to our Dashboard's engine
        column_mapping = {
            'Order Date': 'date',
            'State': 'state_id',
            'City': 'store_id',      # We use City as the Store Node
            'Category': 'cat_id',
            'Product Name': 'item_id',
            'Quantity': 'sales_qty'
        }
        df = df.rename(columns=column_mapping)
        
        # Fix Date Formats
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate Unit Price (Total Sales / Quantity)
        df['sell_price'] = df['Sales'] / df['sales_qty']
        
        # Simulate 'Current Stock' (Since real transaction data doesn't include warehouse inventory)
        np.random.seed(42)
        df['current_stock'] = np.random.randint(20, 200, size=len(df))
        
        return df
    except FileNotFoundError:
        st.error("Data not found! Please run `python download_real_data.py` first.")
        st.stop()

df = load_data()

# -------------------------------------------------------------------------
# 3. HIERARCHICAL FILTERS
# -------------------------------------------------------------------------
st.sidebar.header("Global Warehouse Filters")

states = df['state_id'].dropna().unique()
selected_state = st.sidebar.selectbox("Select Region (State)", sorted(states))

stores = df[df['state_id'] == selected_state]['store_id'].dropna().unique()
selected_store = st.sidebar.selectbox("Select Node (City)", sorted(stores))

categories = df['cat_id'].dropna().unique()
selected_category = st.sidebar.selectbox("Select Product Category", sorted(categories))

filtered_df = df[(df['state_id'] == selected_state) & 
                 (df['store_id'] == selected_store) & 
                 (df['cat_id'] == selected_category)].copy()

if filtered_df.empty:
    st.warning("No sales data available for this specific combination. Please adjust filters.")
    st.stop()

# -------------------------------------------------------------------------
# 4. INVENTORY LOGIC (Top 20 Items for Performance)
# -------------------------------------------------------------------------
LEAD_TIME_DAYS = 3

# Real datasets have thousands of items. We slice the top 20 selling items to keep it clean.
top_items = filtered_df.groupby('item_id')['sales_qty'].sum().nlargest(20).index
inventory_data = []

total_future_demand = 0
total_inventory_value = 0
items_at_risk = 0

for item in top_items:
    item_df = filtered_df[filtered_df['item_id'] == item].sort_values('date')
    
    current_stock = item_df['current_stock'].iloc[-1]
    price = item_df['sell_price'].iloc[-1]
    total_inventory_value += (current_stock * price)
    
    # Heuristic Forecast
    recent_sales = max(1, item_df['sales_qty'].tail(14).mean())
    forecasted_7_day_demand = int(recent_sales * 7 * 1.1) 
    total_future_demand += forecasted_7_day_demand
    
    # Inventory Math
    std_dev = item_df['sales_qty'].std()
    if pd.isna(std_dev): std_dev = 1 # Fallback if only 1 sale exists
    
    safety_stock = int(1.65 * std_dev * np.sqrt(LEAD_TIME_DAYS))
    rop = int((recent_sales * LEAD_TIME_DAYS) + safety_stock)
    
    if current_stock <= rop:
        status = "🔴 Critical: Reorder Now"
        items_at_risk += 1
    elif current_stock <= rop + safety_stock:
        status = "🟡 Warning: Approaching ROP"
    else:
        status = "🟢 Healthy"
        
    inventory_data.append({
        "Item": item[:40] + "..." if len(item) > 40 else item, # Trim long names
        "Price": f"${price:.2f}",
        "Current Stock": current_stock,
        "Safety Stock": safety_stock,
        "ROP": rop,
        "Status": status
    })

# -------------------------------------------------------------------------
# 5. KPI METRIC CARDS
# -------------------------------------------------------------------------
st.markdown("### Regional Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f'<div class="metric-card"><div class="metric-value">${total_inventory_value:,.0f}</div><div class="metric-label">Capital in Inventory</div></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="metric-card"><div class="metric-value">{int(total_future_demand):,} Units</div><div class="metric-label">Projected 7-Day Demand</div></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="metric-card"><div class="metric-value">{len(top_items)}</div><div class="metric-label">Top SKUs Analyzed</div></div>', unsafe_allow_html=True)

risk_color = "#FF4B4B" if items_at_risk > 0 else "#4CAF50"
col4.markdown(f'<div class="metric-card" style="border-color:{risk_color};"><div class="metric-value" style="color:{risk_color};">{items_at_risk}</div><div class="metric-label">SKUs at Stockout Risk</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# 6. INTERACTIVE FORECAST CHART
# -------------------------------------------------------------------------
st.markdown("### 📈 Aggregated Demand: Historical vs. Forecast")

category_history = filtered_df.groupby('date')['sales_qty'].sum().reset_index()
last_14_days = category_history.tail(14)

last_date = last_14_days['date'].max()
future_dates = [last_date + timedelta(days=i) for i in range(1, 8)]
avg_trend = last_14_days['sales_qty'].mean()
future_demand = [max(0, avg_trend + np.random.randint(-5, 5)) for _ in range(7)]

fig = go.Figure()
fig.add_trace(go.Scatter(x=last_14_days['date'], y=last_14_days['sales_qty'], mode='lines+markers', name='Actual History', line=dict(color='#00B4D8', width=3)))
fig.add_trace(go.Scatter(x=future_dates, y=future_demand, mode='lines+markers', name='AI Forecast', line=dict(color='#FF9F1C', width=3, dash='dash')))

fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=30, b=0), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------------------
# 7. ACTIONABLE INVENTORY TABLE
# -------------------------------------------------------------------------
st.markdown("### 📦 SKU-Level Optimization Log (Top Volume Items)")
if inventory_data:
    st.dataframe(pd.DataFrame(inventory_data), use_container_width=True, hide_index=True)
else:
    st.info("No actionable inventory data for this segment.")