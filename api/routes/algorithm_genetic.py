from fastapi import FastAPI, APIRouter, Depends
from api.modules.algorithm_genetic_module import generate_population, function_soma
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

    tam_pop = 1

    populacao = generate_population(tam_pop=tam_pop, db=db) 

    result = populacao

    for i in range(len(populacao)):
        soma = function_soma(populacao[i], db=db)
        print(soma)


    return {"resultado": result}
