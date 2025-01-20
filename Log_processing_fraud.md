# Log Processing System for Real-Time Fraud Detection (Kafka + BigQuery + Django Core API)

## Project Overview
This project implements a real-time log processing system for fraud detection using Apache Kafka, Google BigQuery, and Django Core API. It captures log events, processes them for fraud detection, and stores results in BigQuery for analysis.

## Tech Stack
- **Apache Kafka** - Message broker for real-time log streaming
- **Google BigQuery** - Storage and querying of processed data
- **Django Core API** - Exposing fraud detection results via RESTful API
- **Python** - Main programming language
- **Docker** - Containerization for deployment

## Features
- Real-time log ingestion using Kafka
- Fraud detection logic applied to logs
- Processed logs stored in BigQuery
- API to query fraud detection results

## System Architecture
1. **Log Producer**: Generates and sends log data to Kafka topic.
2. **Log Consumer & Processor**: Consumes logs, applies fraud detection logic, and stores results in BigQuery.
3. **Django API**: Provides endpoints to query fraud detection results.

---

## Step 1: Setup Kafka for Log Streaming

### Install and Start Kafka
```bash
wget https://downloads.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz
tar -xvzf kafka_2.13-3.1.0.tgz
cd kafka_2.13-3.1.0
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties &
```

### Create Kafka Topic
```bash
bin/kafka-topics.sh --create --topic fraud-logs --bootstrap-server localhost:9092
```

---

## Step 2: Implement Log Producer
```python
from kafka import KafkaProducer
import json

def send_log(log_data):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send('fraud-logs', log_data)
    producer.flush()
```

---

## Step 3: Implement Log Consumer & Fraud Detection
```python
from kafka import KafkaConsumer
import json
from google.cloud import bigquery

def process_logs():
    consumer = KafkaConsumer(
        'fraud-logs',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    client = bigquery.Client()
    table_id = 'your_project_id.dataset.logs'
    
    for message in consumer:
        log = message.value
        if detect_fraud(log):
            client.insert_rows_json(table_id, [log])

def detect_fraud(log):
    return log.get("amount", 0) > 1000  # Example fraud condition
```

---

## Step 4: Set Up Django Core API

### Install Django
```bash
pip install django
```

### Create Django Project
```bash
django-admin startproject fraud_detection
cd fraud_detection
python manage.py startapp api
```

### Define Django Model (api/models.py)
```python
from django.db import models

class FraudLog(models.Model):
    user_id = models.CharField(max_length=255)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

### Create API View (api/views.py)
```python
from django.http import JsonResponse
from .models import FraudLog

def get_fraud_logs(request):
    logs = FraudLog.objects.all().values()
    return JsonResponse(list(logs), safe=False)
```

### Define URL Route (fraud_detection/urls.py)
```python
from django.urls import path
from api.views import get_fraud_logs

urlpatterns = [
    path('api/fraud-logs/', get_fraud_logs),
]
```

---

## Step 5: Deploy System with Docker

### Create Dockerfile
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Build and Run
```bash
docker build -t fraud-detection-api .
docker run -p 8000:8000 fraud-detection-api
```

---

## API Usage

### Fetch Fraud Logs
```bash
curl -X GET "http://127.0.0.1:8000/api/fraud-logs/"
```

---

## Conclusion
This project provides a scalable and real-time fraud detection system using Kafka, BigQuery, and Django Core API. It can be extended to include more complex fraud detection mechanisms using ML models.

---

## Future Enhancements
- Implement advanced fraud detection algorithms
- Integrate real-time alerting system
- Deploy on Kubernetes for scalability

