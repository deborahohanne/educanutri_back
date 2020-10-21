from fastapi import FastAPI, APIRouter, Depends
from api.modules.plate_module import generate_plate
from sqlalchemy.orm import Session
from api.model.database import SessionLocal, engine


algoritmo = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@algoritmo.get("/genetic/")
def algoritmo_genetico(idade: int, db: Session = Depends(get_db)):
    '''
        Descrição da API
    '''

    ensino = {"energia": 300, "carboidratos": 48.8, "proteinas": 9.4, "lipideos": 7.5, 
              "fibras": 5.4, "calcio": 210, "ferro": 1.8, "magnesio": 37, "zinco": 1.3}
    fundamental = {"energia": 435, "carboidratos": 70.7, "proteinas": 13.6, "lipideos": 10.9, 
                   "fibras": 6.1, "calcio": 260, "ferro": 2.1, "magnesio": 63, "zinco": 1.8}

    faixa_etaria = {1: ensino, 2: fundamental}

    refeicao = {1: "desjejum", 2: "almoço", 3: "lanche"}

    generate_plate(1, db=db)

    result = faixa_etaria[idade]

    return {"resultado": result}
