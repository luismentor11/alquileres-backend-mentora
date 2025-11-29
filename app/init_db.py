from app.database import engine
from app.models.models import Base

def run():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas con éxito.")

if __name__ == "__main__":
    run()
