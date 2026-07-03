import random

from faker import Faker

from src.database.database import SessionLocal, init_db
from src.database.models import Supplier, Professional, Opportunity

fake = Faker("en_IN")


def seed_database():

    init_db()

    db = SessionLocal()

    # Clear old data
    db.query(Supplier).delete()
    db.query(Professional).delete()
    db.query(Opportunity).delete()

    categories = [
        "Packaging",
        "Logistics",
        "Manufacturing",
        "Raw Material"
    ]

    locations = [
        "Tamil Nadu",
        "Karnataka",
        "Kerala",
        "Telangana",
        "Andhra Pradesh"
    ]

    certifications = [
        "Food Grade",
        "Biodegradable",
        "ISO 9001",
        "FSSAI"
    ]

    # ---------------- Suppliers ---------------- #

    for _ in range(50):

        supplier = Supplier(

            name=fake.company(),

            category=random.choice(categories),

            location=random.choice(locations),

            certification=random.choice(certifications),

            capacity=random.randint(5000, 50000),

            delivery_days=random.randint(5, 40),

            rating=round(random.uniform(3.5, 5.0), 1),

            available=random.choice([True, True, True, False]),

            email=fake.company_email(),

            phone=fake.phone_number(),

            website=fake.url(),

            sustainability_score=round(random.uniform(60, 100), 1),

            price_per_unit=round(random.uniform(5, 50), 2),

            last_updated=str(fake.date())

        )

        db.add(supplier)

    # ---------------- Professionals ---------------- #

    skills = [
        "Procurement",
        "Supply Chain",
        "Vendor Management",
        "Operations"
    ]

    for _ in range(20):

        professional = Professional(

            name=fake.name(),

            skill=random.choice(skills),

            location=random.choice(locations),

            experience=random.randint(1, 15),

            rating=round(random.uniform(3.5, 5), 1),

            email=fake.email(),

            company=fake.company(),

            available=random.choice([True, False])

        )

        db.add(professional)

    # ---------------- Opportunities ---------------- #

    for _ in range(15):

        opportunity = Opportunity(

            title=fake.catch_phrase(),

            category=random.choice(categories),

            budget=random.randint(50000, 1000000),

            location=random.choice(locations),

            description=fake.sentence(),

            deadline=str(fake.date()),

            status=random.choice([
                "Open",
                "Closed",
                "In Progress"
            ])

        )

        db.add(opportunity)

    db.commit()

    db.close()

    print("Database Seeded Successfully!")


if __name__ == "__main__":
    seed_database()