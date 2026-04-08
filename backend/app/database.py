from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import time

DATABASE_URL = "postgresql://admin:admin@db:5432/clients"

# Retry connection logic
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        break
    except Exception:
        print("Database not ready, waiting...")
        time.sleep(2)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()