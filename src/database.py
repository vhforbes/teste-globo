import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "teste-globo")
MYSQL_USER = os.getenv("MYSQL_USER", "teste-globo")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "teste-globo")

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost/{MYSQL_DATABASE}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
