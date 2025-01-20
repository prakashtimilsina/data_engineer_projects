# Project 2: Building a Scalable E-commerce Backend API (Django + PostgreSQL + GCP Cloud Run)

## Overview
This project involves developing a scalable e-commerce backend API using Django, PostgreSQL, and deploying it on GCP Cloud Run. The API will handle product listings, user authentication, order processing, and payments.

## Features
- User authentication (JWT-based authentication)
- Product management (CRUD operations)
- Order management (creating and tracking orders)
- Payment integration (Stripe/PayPal)
- Cloud deployment using GCP Cloud Run

## Tech Stack
- **Backend:** Django
- **Database:** PostgreSQL
- **Deployment:** GCP Cloud Run
- **Authentication:** JWT
- **API Documentation:** Django REST framework (DRF Swagger)

## Setup Instructions

### Prerequisites
- Python 3.x installed
- PostgreSQL installed and configured
- Google Cloud SDK installed and authenticated
- Docker installed

### Step 1: Clone the Repository
```sh
 git clone https://github.com/your-repo/ecommerce-backend.git
 cd ecommerce-backend
```

### Step 2: Set Up Virtual Environment
```sh
 python -m venv venv
 source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```sh
 pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file and add the following:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/ecommerce_db
ALLOWED_HOSTS=*
```

### Step 5: Run Migrations
```sh
 python manage.py migrate
```

### Step 6: Create a Superuser
```sh
 python manage.py createsuperuser
```

### Step 7: Run the Server Locally
```sh
 python manage.py runserver
```

### Step 8: Dockerize the Application
```sh
docker build -t ecommerce-backend .
docker run -p 8000:8000 ecommerce-backend
```

### Step 9: Deploy to GCP Cloud Run
- Build and push the Docker image:
```sh
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/ecommerce-backend
```
- Deploy the service:
```sh
gcloud run deploy ecommerce-backend --image gcr.io/YOUR_PROJECT_ID/ecommerce-backend --platform managed --region us-central1 --allow-unauthenticated
```

### API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and get JWT token |
| GET | `/api/products/` | Get all products |
| POST | `/api/products/` | Create a new product |
| POST | `/api/orders/` | Create an order |
| GET | `/api/orders/` | Get all orders |

### Testing
Run unit tests using:
```sh
python manage.py test
```

## Conclusion
This project demonstrates how to build a scalable and cloud-deployed e-commerce backend using Django, PostgreSQL, and GCP Cloud Run. Feel free to contribute and enhance its functionalities!

---

Feel free to contribute and enhance this project!

---