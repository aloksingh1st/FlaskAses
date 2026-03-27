import requests
from models.customer import Customer


def fetch_all_customers():
    page = 1
    limit = 10
    all_customers = []

    while True:
        url = f"http://localhost:5000/api/customers?page={page}&limit={limit}"
        response = requests.get(url)

        data = response.json()["data"]

        if not data:
            break

        all_customers.extend(data)
        page += 1

    return all_customers


def upsert_customer(db, customer):
    existing = db.query(Customer).filter_by(
        customer_id=customer["customer_id"]
    ).first()

    if existing:
        for key, value in customer.items():
            setattr(existing, key, value)
    else:
        db.add(Customer(**customer))

def ingest_data(db):
    customers = fetch_all_customers()

    for customer in customers:
        upsert_customer(db, customer)

    db.commit()

    return len(customers)