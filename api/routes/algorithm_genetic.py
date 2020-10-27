from fastapi import FastAPI, APIRouter, Depends
from api.modules.algorithm_genetic_module import generate_population, function_nutritional_error
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
def algoritmo_genetico(db: Session = Depends(get_db)):
    '''
        Descrição
    '''

    tam_pop = 2

    populacao = generate_population(tam_pop=tam_pop, db=db) 

    result = populacao

    card_diario = function_nutritional_error(populacao, db=db)

    return {"resultado": card_diario}
