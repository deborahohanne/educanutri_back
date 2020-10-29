from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from api.model import crud, models, schemas
from api.model.database import SessionLocal, engine


alimento = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@alimento.post("/alimento/criar/", response_model=schemas.Alimento)
def create_food(alimento: schemas.AlimentoCreate, db: Session = Depends(get_db)):
    alimento = crud.create_food(db=db, alimento=alimento)
    return alimento


@alimento.get("/alimento/buscar/", response_model=List[schemas.Alimento])
def read_food(db: Session = Depends(get_db)):
    alimentos = crud.get_foods_all(db)
    return alimentos


@alimento.get("/alimento/buscar/{alimento_id}")
def read_food_by_id(alimento_id: int, db: Session = Depends(get_db)):
    alimento = crud.get_food_by_id(db, alimento_id)
    return alimento


@alimento.delete("/alimento/deletar/{alimento_id}")
def delete_food(alimento_id: int, db: Session = Depends(get_db)):
    if crud.delete_food(db, alimento_id):
        return {"message": f'O alimento {alimento_id} foi deletado!'}
    else:
        return {"message": f'O alimento {alimento_id} não foi encontrado!'}