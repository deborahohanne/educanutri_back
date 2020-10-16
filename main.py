from api.routes import algoritmo_genetico
import uvicorn
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from api.model.export_data import data_alimentos
from api.model import crud, models, schemas
from api.model.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Educanutri API",
    description="API Educanutri",
    version='0.1.0'
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def index():
    return {"Welcome Educanutri"}


@app.post("/alimento/", response_model=schemas.Alimento)
def create_alimento(alimento: schemas.AlimentoCreate, db: Session = Depends(get_db)):
    return crud.create_alimento(db=db, alimento=alimento)


@app.post("/prato/", response_model=schemas.Prato)
def create_prato(prato: schemas.PratoCreate, db: Session = Depends(get_db)):
    return crud.create_prato(db=db, prato=prato)


@app.get("/alimentos/", response_model=List[schemas.Alimento])
def read_alimentos(db: Session = Depends(get_db)):
    alimentos = crud.get_alimentos_all(db)
    return alimentos

@app.get("/pratos/", response_model=schemas.Prato)
def read_pratos(db: Session = Depends(get_db)):
    pratos = crud.get_pratos_all(db)
    return pratos

def retrieve_alimento(db: Session, alimento_id: int):
    return db.query(models.Alimento).filter(models.Alimento.id == alimento_id).first()

@app.delete("/alimento/{alimento_id}")
def delete_alimento(alimento_id: int, db: Session = Depends(get_db)):
    alimento = retrieve_alimento(db, alimento_id)
    if alimento:
        db.delete(alimento)
        db.commit()
        return True
    return False


@app.get("/export_data/")
def export_data(db: Session = Depends(get_db)):
    data_alimentos.export_data(db)


app.include_router(algoritmo_genetico.algoritmo, tags=['Algoritmo genético'])



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
