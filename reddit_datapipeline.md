# Reddit Data Pipeline for Topic Modeling

## 📌 Project Overview
This project builds a **Reddit Data Pipeline** using **GCP Dataflow, BigQuery, and Airflow** to extract, transform, and analyze Reddit data for **topic modeling**. The pipeline collects posts and comments from Reddit, processes them using Apache Beam, stores the cleaned data in BigQuery, and applies NLP techniques to identify trending topics.

---

## 🚀 Technologies Used
- **Google Cloud Platform (GCP)**
  - Dataflow (Apache Beam)
  - BigQuery
  - Cloud Storage
  - Cloud Composer (Managed Airflow)
- **Python**
- **Apache Beam**
- **Airflow**
- **Reddit API (PRAW)**
- **Natural Language Processing (NLP)**

---

## 📁 Project Structure
```bash
reddit-data-pipeline/
│── dags/
│   ├── reddit_pipeline.py       # Airflow DAG for orchestrating the pipeline
│── dataflow/
│   ├── process_reddit.py        # Apache Beam script for data transformation
│── models/
│   ├── topic_modeling.py        # NLP model for topic extraction
│── config/
│   ├── settings.yaml            # Configuration file for API keys and GCP settings
│── scripts/
│   ├── fetch_reddit_data.py     # Script to fetch data from Reddit API
│── requirements.txt             # Required dependencies
│── README.md                    # Project Documentation
```

---

## 🎯 Key Features
✅ **Automated Reddit Data Extraction**: Uses the Reddit API to collect posts & comments.
✅ **Streaming & Batch Processing**: Apache Beam processes data efficiently on Dataflow.
✅ **BigQuery Integration**: Stores structured Reddit data for analysis.
✅ **Topic Modeling with NLP**: Identifies key discussion topics using machine learning.
✅ **Orchestration with Airflow**: Automates and schedules the ETL pipeline.

---

## 🔧 Setup and Deployment

### 1️⃣ Prerequisites
- Google Cloud Project with **BigQuery**, **Dataflow**, and **Cloud Composer** enabled.
- Reddit API credentials (client ID & secret from [Reddit Developer Portal](https://www.reddit.com/dev/api/)).
- Python 3.8+

### 2️⃣ Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/reddit-data-pipeline.git
cd reddit-data-pipeline
```
Install dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Configuration
Update the `config/settings.yaml` file with:
```yaml
reddit:
  client_id: "your_client_id"
  client_secret: "your_client_secret"
  user_agent: "your_user_agent"
  subreddit: "technology"

gcp:
  project_id: "your_gcp_project"
  bigquery_dataset: "reddit_dataset"
  bigquery_table: "posts"
```

### 4️⃣ Running the Pipeline
#### Run Dataflow Job:
```bash
python dataflow/process_reddit.py --runner DataflowRunner --project your_gcp_project
```
#### Deploy Airflow DAG:
Upload `dags/reddit_pipeline.py` to Cloud Composer DAGs folder:
```bash
gsutil cp dags/reddit_pipeline.py gs://your-composer-bucket/dags/
```
Trigger the DAG from the Airflow UI.

---

## 📊 Data Schema (BigQuery)
| Column Name   | Type      | Description                   |
|--------------|----------|-------------------------------|
| post_id      | STRING   | Unique ID of the post        |
| title        | STRING   | Title of the post            |
| body         | STRING   | Post content                 |
| author       | STRING   | Username of the author       |
| created_utc  | TIMESTAMP | Post creation timestamp      |
| subreddit    | STRING   | Subreddit name               |
| num_comments | INTEGER  | Number of comments           |
| upvotes      | INTEGER  | Number of upvotes            |

---

## 📌 Future Enhancements
🔹 **Implement Real-Time Processing** using Pub/Sub & Dataflow Streaming.
🔹 **Enhance Topic Modeling** with LDA or BERT-based embeddings.
🔹 **Develop a Dashboard** in **Looker Studio** for data visualization.

---


Feel free to contribute and enhance this project!

---