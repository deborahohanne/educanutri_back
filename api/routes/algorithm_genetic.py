from fastapi import FastAPI, APIRouter


algoritmo = APIRouter()


@algoritmo.get("/genetic")
def algoritmo_genetico(idade_inicial: int, idade_final: int):
    '''
        Descrição da API
    '''
    idade_inicial = idade_inicial
    idade_final = idade_final

    return {"idade_incial": idade_inicial, "idade_final": idade_final}


