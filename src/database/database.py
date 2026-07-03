from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path

# Database folder
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# SQLite database path
DATABASE_URL = f"sqlite:///{DATA_DIR / 'suproc.db'}"

# SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

# Base Model
Base = declarative_base()


def init_db():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)