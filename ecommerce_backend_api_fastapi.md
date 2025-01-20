# Building a Scalable E-commerce Backend API (FastAPI + PostgreSQL + GCP Cloud Run)

## Project Overview
This project focuses on building a scalable e-commerce backend API using FastAPI, PostgreSQL, and deploying it on Google Cloud Run. The API handles user authentication, product listings, order management, and payment processing.

## Features
- User Authentication (JWT-based)
- Product Catalog Management
- Shopping Cart and Checkout Process
- Order Management
- Payment Processing Integration
- Scalable Deployment on GCP Cloud Run

## Tech Stack
- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **Cloud Provider**: Google Cloud Platform (GCP)
- **Deployment**: GCP Cloud Run
- **Authentication**: JWT
- **Payment Gateway**: Stripe (or any preferred provider)

## Prerequisites
- Python 3.9+
- PostgreSQL database
- Google Cloud SDK installed
- Stripe API key (for payment processing)

## Step-by-Step Implementation

### 1. Set Up Project Environment
```bash
mkdir ecommerce-backend
cd ecommerce-backend
python -m venv venv
source venv/bin/activate
pip install fastapi[all] psycopg2 pydantic
```

### 2. Initialize FastAPI Application
Create `main.py`:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to E-commerce API"}
```

Run the app:
```bash
uvicorn main:app --reload
```

### 3. Database Setup (PostgreSQL)
Update `database.py`:
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/ecommerce_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
```

### 4. Implement Authentication
Add JWT authentication using `auth.py`:
```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return {"user": "sample_user"}  # Implement JWT decoding logic
```

### 5. Create API Endpoints (Products, Orders, Users)
Example: `routes/products.py`
```python
from fastapi import APIRouter
router = APIRouter()

@router.get("/products")
def get_products():
    return [{"id": 1, "name": "Laptop", "price": 999.99}]
```

### 6. Containerize with Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### 7. Deploy on GCP Cloud Run
```bash
gcloud builds submit --tag gcr.io/your-project-id/ecommerce-api
gcloud run deploy ecommerce-api --image gcr.io/your-project-id/ecommerce-api --platform managed
```

### 8. Testing & Monitoring
- Use **Postman** to test API endpoints
- Set up **GCP Logging & Monitoring** for Cloud Run

## Future Enhancements
- Implement Redis caching
- Add WebSocket for real-time order tracking
- Integrate AI-based product recommendations

## License
This project is licensed under the MIT License.

---

### Contributors
- **Your Name** - [GitHub Profile](https://github.com/yourgithubhandle)

Happy Coding! 🚀

