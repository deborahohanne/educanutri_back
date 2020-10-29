from fastapi import FastAPI, APIRouter, Depends
from api.model import crud, models, schemas
from sqlalchemy.orm import Session
from typing import List

from api.model.database import SessionLocal, engine


prato = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@prato.post("/prato/criar/", response_model=schemas.Prato)
def create_plate(prato: schemas.PratoCreate, db: Session = Depends(get_db)):
    prato = crud.create_plate(db=db, prato=prato)
    return prato


@prato.get("/prato/buscar/", response_model=List[schemas.Prato])
def read_plate(db: Session = Depends(get_db)):
    pratos = crud.get_plates_all(db)
    return pratos

@prato.get("/prato/buscar/{prato_id}")
def read_plate_by_id(prato_id: int, db: Session = Depends(get_db)):
    prato = crud.get_plate_by_id(db, prato_id)
    return prato


@prato.post("/prato/adicionar/alimento/", response_model=schemas.Criacao)
def add_plate(criacao: schemas.CriacaoCreate, db: Session = Depends(get_db)):
    return crud.create_creation(db=db, criacao=criacao)


@prato.delete("/prato/deletar/{prato_id}")
def delete_plate(prato_id: int, db: Session = Depends(get_db)):
    if crud.delete_plate(db, prato_id):
        return {"message": f'O prato {prato_id} foi deletado!'}
    else:
        return {"message": f'O prato {prato_id} não foi encontrado!'}
