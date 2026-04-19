# 🌍 Global Retail Supply Chain & Inventory AI Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75.svg)

> **Live Demo:** [Link to your deployed app or a GIF demo here]

An enterprise-grade Data Science and Supply Chain analytics platform built to optimize inventory replenishment, dynamically calculate safety stock, and forecast demand using real-world retail data.

---

## 🚀 Project Overview

Retailers constantly balance between two costly extremes: **stockouts** (which lose immediate revenue and damage customer trust) and **overstocking** (which ties up capital in warehousing costs). 

This project solves this optimization problem by building a dynamic, hierarchical dashboard that analyzes transaction history, forecasts future demand, and generates automated, SKU-level Reorder Point (ROP) alerts.

### 💼 Business Value & Industry Relevance
* **Mitigates the Bullwhip Effect:** Provides data-driven visibility into regional nodes (State $\rightarrow$ City $\rightarrow$ Category).
* **Capital Efficiency:** Identifies exactly how much capital is tied up in current inventory.
* **Service Level Assurance:** Uses mathematical standard deviation to calculate Safety Stock, ensuring a high service level even during demand volatility.

---

## 🧠 System Architecture & Workflow

### The Pipeline
1. **Data Ingestion:** Programmatic retrieval of the 50,000+ row Global Superstore dataset.
2. **Preprocessing Engine:** Cleans anomalies, standardizes date-time formats, and calculates item-level unit economics.
3. **Forecasting Engine:** Aggregates historical time-series data to project a 7-day rolling demand curve.
4. **Inventory Math Logic:** * `Safety Stock = Z-Score * Standard Deviation of Demand * √Lead Time`
   * `Reorder Point (ROP) = (Average Daily Sales * Lead Time) + Safety Stock`
5. **Interactive UI:** Renders KPI metrics, Plotly visualizations, and actionable alert tables via Streamlit.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Frontend UI:** Streamlit (Custom CSS injected for Dark Mode Enterprise styling)
* **Data Engineering:** Pandas, NumPy
* **Data Visualization:** Plotly Graph Objects
* **Version Control:** Git & GitHub

---

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
