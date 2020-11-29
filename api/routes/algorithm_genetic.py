from fastapi import FastAPI, APIRouter, Depends
from api.modules.algorithm_genetic_module import generate_population, function_fitness, function_selection, crossover, \
    mutation
from sqlalchemy.orm import Session
from api.model.database import SessionLocal, engine

algoritmo = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@algoritmo.get("/genetic/{tam_pop}/{qtd_dias}")
def algoritmo_genetico(tam_pop: int, qtd_dias: int, db: Session = Depends(get_db)):
    """
        Descrição: Rota responsável por gerar os cardápios semanais.
    """
    final = []
    
    print(qtd_dias)

    for _ in range(qtd_dias):
        populacao = generate_population(tam_pop=tam_pop, db=db)

        result = populacao

        while len(result) > 1:
            fitness, qtd_ind = function_fitness(result, db=db)

            selecao = function_selection(fitness, qtd_ind)

            cruzados = crossover(selecao)

            result = mutation(cruzados, db=db)

        final.append(result)

    return {"resultado": final}
