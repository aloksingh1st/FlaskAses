from fastapi import FastAPI
from database import SessionLocal
from services.ingestion import ingest_data
from fastapi import Query
import time

time.sleep(10)

app = FastAPI()

from database import engine, Base
from models.customer import Customer

Base.metadata.create_all(bind=engine)




@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/ingest")
def ingest():
    db = SessionLocal()

    try:
        count = ingest_data(db)
        return {"status": "success", "records_processed": count}
    finally:
        db.close()


@app.get("/api/customers")
def get_customers(page: int = Query(1), limit: int = Query(10)):
    db = SessionLocal()

    offset = (page - 1) * limit

    customers = db.query(Customer).offset(offset).limit(limit).all()

    total = db.query(Customer).count()

    db.close()

    return {
        "data": customers,
        "total": total,
        "page": page,
        "limit": limit
    }


@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: str):
    db = SessionLocal()

    customer = db.query(Customer).filter_by(customer_id=customer_id).first()

    db.close()

    if not customer:
        return {"error": "Customer not found"}, 404

    return customer