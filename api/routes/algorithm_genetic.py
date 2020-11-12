from fastapi import FastAPI, APIRouter, Depends
from api.modules.algorithm_genetic_module import generate_population, function_fitness, function_selection, crossover
from sqlalchemy.orm import Session
from api.model.database import SessionLocal, engine


algoritmo = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@algoritmo.get("/genetic/{tam_pop}/{valor_max}")
def algoritmo_genetico(tam_pop: int, valor_max: float, db: Session = Depends(get_db)):
    '''
        Descrição: Rota responsável por gerar os cardápios semanais.
    '''

    populacao = generate_population(tam_pop=tam_pop, db=db) 

    fitness = function_fitness(valor_max, populacao, db=db)

    selecao = function_selection(fitness)

    cruzados = crossover(selecao)

    result = cruzados
    
    return {"resultado": result}
