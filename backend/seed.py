from app.db.session import SessionLocal
from app.models.hcp import HCP

seed_data = [
    {"name": "Dr. Amit Sharma", "specialty": "Cardiology", "hospital": "City Heart Center", "city": "Mumbai"},
    {"name": "Dr. Neha Iyer", "specialty": "Endocrinology", "hospital": "Metro Clinic", "city": "Bengaluru"},
    {"name": "Dr. Raj Malhotra", "specialty": "Oncology", "hospital": "Hope Cancer Institute", "city": "Delhi"},
    {"name": "Dr. Priya Nair", "specialty": "Neurology", "hospital": "NeuroCare Hospital", "city": "Chennai"},
    {"name": "Dr. Sameer Khan", "specialty": "General Medicine", "hospital": "Sunrise Health", "city": "Hyderabad"},
]

db = SessionLocal()
try:
    for row in seed_data:
        exists = db.query(HCP).filter(HCP.name == row["name"]).first()
        if not exists:
            db.add(HCP(**row))
    db.commit()
    print("✅ Seed completed")
finally:
    db.close()