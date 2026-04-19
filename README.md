# 🌍 Global Retail Supply Chain & Inventory AI Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75.svg)

> **Live Demo:** [Link to your deployed app or a GIF demo here]

An enterprise-grade Data Science and Supply Chain analytics platform built to optimize inventory replenishment, dynamically calculate safety stock, and forecast demand using real-world retail data.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Project Overview

Retailers constantly balance between two costly extremes: **stockouts** (which lose immediate revenue and damage customer trust) and **overstocking** (which ties up capital in warehousing costs). 

This project solves this optimization problem by building a dynamic, hierarchical dashboard that analyzes transaction history, forecasts future demand, and generates automated, SKU-level Reorder Point (ROP) alerts.

### 💼 Business Value & Industry Relevance
* **Mitigates the Bullwhip Effect:** Provides data-driven visibility into regional nodes (State $\rightarrow$ City $\rightarrow$ Category).
* **Capital Efficiency:** Identifies exactly how much capital is tied up in current inventory.
* **Service Level Assurance:** Uses mathematical standard deviation to calculate Safety Stock, ensuring a high service level even during demand volatility.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 System Architecture & Workflow

### The Pipeline
1. **Data Ingestion:** Programmatic retrieval of the 50,000+ row Global Superstore dataset.
2. **Preprocessing Engine:** Cleans anomalies, standardizes date-time formats, and calculates item-level unit economics.
3. **Forecasting Engine:** Aggregates historical time-series data to project a 7-day rolling demand curve.
4. **Inventory Math Logic:** * `Safety Stock = Z-Score * Standard Deviation of Demand * √Lead Time`
   * `Reorder Point (ROP) = (Average Daily Sales * Lead Time) + Safety Stock`
5. **Interactive UI:** Renders KPI metrics, Plotly visualizations, and actionable alert tables via Streamlit.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack

* **Language:** Python 3
* **Frontend UI:** Streamlit (Custom CSS injected for Dark Mode Enterprise styling)
* **Data Engineering:** Pandas, NumPy
* **Data Visualization:** Plotly Graph Objects
* **Version Control:** Git & GitHub

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Folder Structure

```text
global-retail-inventory-ai/
│
├── app/
│   └── main_dashboard.py      # The core Streamlit application and UI logic
│
├── data/
│   └── raw/                   # Auto-generated folder for dataset storage (Ignored by Git)
│
├── download_real_data.py      # Automated data extraction script
├── requirements.txt           # Python dependencies
├── .gitignore                 # Excludes venv and large data files
└── README.md                  # Project documentation
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
💻 Installation & Execution
git clone [https://github.com/YourUsername/global-retail-inventory-ai.git](https://github.com/YourUsername/global-retail-inventory-ai.git)
cd global-retail-inventory-ai

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
▶️Run the  Projecct
python download_real_data.py
streamlit run app/main_dashboard.py
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
📊 Visual Walkthrough
1. The Global Overview
<img width="1919" height="564" alt="Screenshot 2026-04-19 163829" src="https://github.com/user-attachments/assets/9df6fe4d-f18a-4691-8d2a-7cc62b606c83" />
<img width="1490" height="636" alt="Screenshot 2026-04-19 163846" src="https://github.com/user-attachments/assets/b341e840-5bfb-47e8-8cf8-7d596d62c875" />
<img width="1443" height="206" alt="Screenshot 2026-04-19 163918" src="https://github.com/user-attachments/assets/30258d43-0873-47ba-ade8-4a13bb8723b1" />

The executive view tracks total capital tied in inventory and flags regional nodes at risk of stockouts.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Hierarchical Filtering & Forecasting
(Add a GIF here showing you clicking the dropdowns and the Plotly graph updating)

Users can drill down from the State level to specific Cities and Categories. The interactive time-series chart overlays historical actuals with projected demand.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. SKU-Level Action Log
(Add a screenshot here of the dataframe table with the red and green status dots)

The system evaluates current stock against the dynamic ROP. SKUs falling below the threshold trigger a "🔴 Critical: Reorder Now" alert.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
🔮 Future Improvements
To scale this Minimum Viable Product (MVP) into a production-ready application, the following architectural upgrades are planned:

Cloud Database Integration: Migrate from CSV ingestion to querying a live PostgreSQL or Snowflake data warehouse.

Advanced ML Models: Implement an isolated FastAPI backend hosting a serialized XGBoost or Prophet model to replace the current fast-heuristic forecasting logic.

Containerization: Package the application using Docker for scalable Kubernetes deployment.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
🎓 Learning Outcomes
Building this project provided deep, hands-on experience with:

Processing and translating unstructured, real-world data schemas.

Translating supply chain business logic (Safety Stock, ROP) into executable Python code.

Designing user-centric, responsive dashboards for non-technical business stakeholders.

Managing enterprise project architecture and version control best practices.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Designed and engineered by Swijay Singh
