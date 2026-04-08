from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from .models import Base, Client
from .schemas import ClientCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Nivel 1 API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clients")
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

@app.get("/clients")
def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()