# Real-Time Stock Market Data Pipeline using GCP & Apache Beam

## 📌 Project Overview
This project builds a **real-time stock market data pipeline** using **Google Cloud Platform (GCP), Apache Beam, Kafka, and Apache Airflow**. The pipeline streams live stock prices, processes the data, and stores it in **BigQuery** for analysis.

---

## 🚀 Tech Stack
- **Google Cloud Platform (GCP)**: BigQuery, Pub/Sub, Cloud Storage, Dataflow, Composer (Airflow)
- **Apache Kafka**: Real-time messaging
- **Apache Beam**: ETL data processing
- **Apache Airflow**: Workflow orchestration
- **Python**: Scripting and data processing
- **Looker Studio**: Visualization & reporting

---

## 🎯 Features
✅ Real-time stock price ingestion from a simulated stock market feed
✅ Data validation and transformation using Apache Beam
✅ Automatic table creation in BigQuery
✅ Batch and streaming mode support
✅ Airflow DAG for automated scheduling
✅ Interactive dashboard using Looker Studio

---

## 📁 Folder Structure
```
📂 real-time-stock-pipeline
│── 📂 scripts
│   ├── producer.py  # Simulated stock market feed
│   ├── consumer.py  # Kafka consumer (optional)
│── 📂 apache_beam
│   ├── etl_pipeline.py  # Apache Beam ETL pipeline
│── 📂 airflow_dags
│   ├── stock_data_pipeline.py  # Airflow DAG
│── 📂 config
│   ├── config.yaml  # GCP and Kafka settings
│── README.md
```

---

## 🛠️ Setup & Installation

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/real-time-stock-pipeline.git
cd real-time-stock-pipeline
```

### 🔹 Step 2: Install Dependencies
```bash
pip install apache-beam[gcp] google-cloud-bigquery google-cloud-pubsub apache-airflow kafka-python
```

### 🔹 Step 3: Setup Google Cloud Platform (GCP)
- **Enable APIs**: BigQuery, Pub/Sub, Dataflow, Cloud Storage, Cloud Composer
- **Create BigQuery Dataset & Table**:
```sql
CREATE TABLE stock_analysis.stock_prices (
  timestamp TIMESTAMP,
  symbol STRING,
  price FLOAT64,
  volume INT64
);
```
- **Create a Pub/Sub Topic**:
```bash
gcloud pubsub topics create stock-prices
gcloud pubsub subscriptions create stock-sub --topic=stock-prices
```

---

## 📡 Data Ingestion with Kafka or Pub/Sub
### 🔹 Run Kafka Producer (Simulated Stock Data Stream)
```bash
python scripts/producer.py
```
### 🔹 Run Kafka Consumer (Optional for Debugging)
```bash
python scripts/consumer.py
```

---

## 🔄 Data Processing with Apache Beam (Dataflow)
### 🔹 Run ETL Pipeline Locally
```bash
python apache_beam/etl_pipeline.py --runner DirectRunner
```
### 🔹 Deploy to Google Cloud Dataflow
```bash
python apache_beam/etl_pipeline.py --runner DataflowRunner --project your-gcp-project --temp_location gs://your-bucket/temp/
```

---

## 📅 Automate with Apache Airflow (Cloud Composer)
### 🔹 Upload DAG to Airflow
```bash
cp airflow_dags/stock_data_pipeline.py ~/airflow/dags/
```
### 🔹 Start Airflow Scheduler
```bash
airflow scheduler &
airflow webserver &
```

---

## 📊 Analyzing Data in BigQuery
### 🔹 Query Stock Prices
```sql
SELECT symbol, AVG(price) AS avg_price, MAX(price) AS max_price
FROM stock_analysis.stock_prices
GROUP BY symbol;
```

---

## 📈 Visualizing with Looker Studio
1. Connect **BigQuery** to **Looker Studio**
2. Create **Real-time Stock Price Dashboard**
3. Add **Price Trends, Volume Analysis, Moving Averages**

---

## 🔥 Next Steps
✅ Deploy on **GKE (Kubernetes)**
✅ Implement **ML-based price forecasting**
✅ Add **real-time alert notifications**



