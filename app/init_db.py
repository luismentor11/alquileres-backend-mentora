from app.database import Base, engine
from app.models import models


def init_db():
    # Importar modelos asegura que se registren en Base.metadata
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
