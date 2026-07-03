import uuid

from sqlalchemy import Column, String, Integer, Float, Boolean
from src.database.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    location = Column(String, nullable=False)

    certification = Column(String)

    capacity = Column(Integer)

    delivery_days = Column(Integer)

    rating = Column(Float)

    available = Column(Boolean, default=True)

    email = Column(String)

    phone = Column(String)

    website = Column(String)

    sustainability_score = Column(Float)

    price_per_unit = Column(Float)

    last_updated = Column(String)


class Professional(Base):
    __tablename__ = "professionals"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String, nullable=False)

    skill = Column(String)

    location = Column(String)

    experience = Column(Integer)

    rating = Column(Float)

    email = Column(String)

    company = Column(String)

    available = Column(Boolean, default=True)


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    title = Column(String)

    category = Column(String)

    budget = Column(Integer)

    location = Column(String)

    description = Column(String)

    deadline = Column(String)

    status = Column(String)