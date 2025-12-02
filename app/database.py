from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Tomamos los valores que Railway ya define para Postgres
DB_USER = os.getenv("PGUSER") or os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("PGPASSWORD") or os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("PGHOST", "postgres.railway.internal")
DB_PORT = os.getenv("PGPORT", "5432")
DB_NAME = os.getenv("PGDATABASE") or os.getenv("POSTGRES_DB") or "railway"

# Armamos la URL completa a partir de esas variables
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
