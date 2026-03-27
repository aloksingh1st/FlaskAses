# Backend Data Pipeline Assessment

## 🚀 Overview

This project implements a simple data pipeline using three services:

* **Flask (Mock Server)** → serves customer data from a JSON file
* **FastAPI (Pipeline Service)** → ingests and processes data
* **PostgreSQL (Database)** → stores customer records

**Flow:**
Flask API → FastAPI ingestion → PostgreSQL → API responses

---

## 🧱 Project Structure

```
project-root/
├── docker-compose.yml
├── README.md
├── mock-server/
│   ├── app.py
│   ├── data/customers.json
│   ├── Dockerfile
│   └── requirements.txt
└── pipeline-service/
    ├── main.py
    ├── models/customer.py
    ├── services/ingestion.py
    ├── database.py
    ├── Dockerfile
    └── requirements.txt
```

---

## ⚙️ Services

### 1. Flask Mock Server (Port 5000)

* Serves customer data from JSON file
* Supports pagination
* Endpoints:

  * `GET /api/customers?page=&limit=`
  * `GET /api/customers/{id}`
  * `GET /api/health`

---

### 2. FastAPI Pipeline Service (Port 8000)

* Fetches data from Flask API
* Handles pagination automatically
* Performs **upsert** into PostgreSQL
* Endpoints:

  * `POST /api/ingest`
  * `GET /api/customers?page=&limit=`
  * `GET /api/customers/{id}`

---

### 3. PostgreSQL (Port 5432)

* Stores customer records
* Table: `customers`

---

## 🐳 How to Run

### Step 1: Start all services

```bash
docker-compose up --build
```

---

### ⚠️ If build fails

Sometimes images or dependencies may not be pulled properly.

Try this:

```bash
docker-compose pull
docker-compose up --build
```

---

## 🧪 Testing the Pipeline

### 1. Test Flask API

```bash
curl "http://localhost:5000/api/customers?page=1&limit=5"
```

---

### 2. Run ingestion

```bash
curl -X POST http://localhost:8000/api/ingest
```

Expected:

```json
{
  "status": "success",
  "records_processed": 20
}
```

---

### 3. Fetch data from DB via FastAPI

```bash
curl "http://localhost:8000/api/customers?page=1&limit=5"
```

---

### 4. Get single customer

```bash
curl http://localhost:8000/api/customers/C001
```

---

## 🧠 Design Decisions

* **Pagination Loop**
  Uses dynamic fetching (`while loop`) instead of fixed page count

* **Upsert Logic**
  Prevents duplicates and keeps records updated

* **Service Communication**
  Uses Docker internal networking (`mock-server`, `postgres`)

---

## 📌 Notes

* Flask loads data from JSON (not hardcoded)
* FastAPI uses SQLAlchemy ORM
* Docker Compose orchestrates all services
* Clean modular structure for scalability

---

## ✅ Submission Checklist

* [x] All services run using `docker-compose up --build`
* [x] Flask API working with pagination
* [x] FastAPI ingestion working
* [x] PostgreSQL storing data correctly
* [x] All endpoints functional

---

## 👨‍💻 Author

Backend Developer Assessment Submission
ALOK SINGH
9335929565
https://github.com/aloksingh1st# FlaskAses
