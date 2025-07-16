# 🧠 Complaint Intelligence Dashboard

An interactive Streamlit dashboard that analyzes consumer complaints submitted to U.S. financial institutions using sentiment analysis, time trends, and key regulatory metrics.

Built to simulate a data analyst role in the financial services sector (e.g. HSBC), this project helps surface patterns in customer experience and complaint handling performance using publicly available data.

---

## 🔍 Features

- 📊 **Complaint Volume Trends**: Track complaints over time using monthly resampling
- 💬 **Sentiment Analysis**: Applied VADER to classify complaint narratives into Positive, Neutral, or Negative
-  **Interactive Filters**: Slice data by Product, Issue Type, and Sentiment
-  **Regulatory KPIs**: Calculate % Timely Response and % Disputed flags per company
-  **Streamlit UI**: Built a clean, lightweight dashboard using Streamlit with sidebar filters and auto-updating charts

---

## 🗂️ Dataset

**Source**: [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)  
Subset used: Complaints against major banks like JPMorgan Chase and Bank of America (CSV extracted)

---

## 🚀 How to Run the App

### 📦 Install Requirements
```bash
pip install -r requirements.txt




