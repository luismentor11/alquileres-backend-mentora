from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base de datos SQLite local dentro del contenedor
DATABASE_URL = "sqlite:///./alquileres.db"

Base = declarative_base()

# Para SQLite hay que agregar connect_args de esta forma
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
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
