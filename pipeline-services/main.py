from fastapi import FastAPI
from database import SessionLocal
from services.ingestion import ingest_data
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