# ETL Pipeline for Twitter Sentiment Analysis

## Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline for Twitter sentiment analysis using Python, Google BigQuery, and Apache Airflow. The pipeline fetches tweets, processes them for sentiment analysis, and stores the results in BigQuery for further analysis.

## Tech Stack
- **Python**: Data extraction and processing
- **Google BigQuery**: Data storage and querying
- **Apache Airflow**: Workflow orchestration
- **Twitter API**: Data source for tweets
- **NLTK/VADER**: Sentiment analysis

## Architecture
1. **Extract**: Fetch tweets using the Twitter API.
2. **Transform**: Process tweets, clean text, and apply sentiment analysis.
3. **Load**: Store processed data in BigQuery.
4. **Orchestration**: Use Apache Airflow to schedule and monitor pipeline execution.

## Setup Instructions
### 1. Environment Setup
- Install dependencies:
  ```sh
  pip install apache-airflow google-cloud-bigquery tweepy nltk
  ```
- Set up Google Cloud credentials:
  ```sh
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
  ```
- Configure Airflow:
  ```sh
  export AIRFLOW_HOME=~/airflow
  airflow db init
  airflow users create --username admin --password admin --role Admin --email admin@example.com
  ```

### 2. Twitter API Setup
- Sign up at [Twitter Developer Portal](https://developer.twitter.com/).
- Generate API keys and tokens.
- Store credentials in `.env` file:
  ```sh
  TWITTER_API_KEY=your_api_key
  TWITTER_API_SECRET=your_api_secret
  TWITTER_ACCESS_TOKEN=your_access_token
  TWITTER_ACCESS_SECRET=your_access_secret
  ```

### 3. BigQuery Setup
- Create a dataset in BigQuery.
- Define schema for storing tweets and sentiment scores.

### 4. Implement the ETL Pipeline
#### Extract Tweets
```python
import tweepy

def fetch_tweets():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q="Python", count=100)
    return tweets
```
#### Transform: Sentiment Analysis
```python
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(tweet):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(tweet)
    return score['compound']
```
#### Load: Store Data in BigQuery
```python
from google.cloud import bigquery

def load_to_bigquery(data):
    client = bigquery.Client()
    dataset_ref = client.dataset("twitter_sentiment")
    table_ref = dataset_ref.table("tweets")
    client.insert_rows_json(table_ref, data)
```

### 5. Airflow DAG
Create an Airflow DAG to automate the ETL process:
```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def etl_pipeline():
    tweets = fetch_tweets()
    processed_data = [{"tweet": t.text, "sentiment": analyze_sentiment(t.text)} for t in tweets]
    load_to_bigquery(processed_data)

default_args = {"owner": "airflow", "start_date": datetime(2024, 1, 1)}

dag = DAG("twitter_etl", default_args=default_args, schedule_interval="@daily")

etl_task = PythonOperator(task_id="run_etl", python_callable=etl_pipeline, dag=dag)
```

### 6. Running the Pipeline
- Start Airflow scheduler and webserver:
  ```sh
  airflow scheduler & airflow webserver
  ```
- Trigger the DAG:
  ```sh
  airflow dags trigger twitter_etl
  ```

## Future Enhancements
- Integrate more advanced NLP techniques (e.g., BERT, GPT-based sentiment analysis)
- Implement real-time streaming using Kafka
- Visualize sentiment trends using Looker Studio or Tableau

## Conclusion
This ETL pipeline efficiently extracts, processes, and loads Twitter sentiment data into BigQuery. It serves as a scalable and automated solution for sentiment analysis tasks.

---

Feel free to contribute and enhance this project!

