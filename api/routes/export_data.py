from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session

from api.model import crud, models, schemas
from api.model.export_data import data_alimentos
from api.model.database import SessionLocal, engine

data = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@data.get("/export_data/")
def export_data(db: Session = Depends(get_db)):
    data_alimentos.export_data(db)

