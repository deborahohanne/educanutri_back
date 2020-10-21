from sqlalchemy.orm import Session
from api.model import crud, models, schemas, search
from api.model.database import SessionLocal

from random import randint


def generate_plate(refeicao: int, db: Session):

    lista_refeicoes = []

    if refeicao == 1:
        fruta = search.search_plate(db=db, tipo=8)
        leite_der = search.search_plate(db=db, tipo=7)
        pao_cereal = search.search_plate(db=db, tipo=8)

        lista_refeicoes.append(fruta)
        lista_refeicoes.append(leite_der)
        lista_refeicoes.append(pao_cereal)

    elif refeicao == 2:
        acomp_arroz = search.search_plate(db=db, tipo=1)
        acomp_feijao = search.search_plate(db=db, tipo=2)
        entrada = search.search_plate(db=db, tipo=3)
        guarnicao = search.search_plate(db=db, tipo=4)
        principal = search.search_plate(db=db, tipo=5)
        sobremesa = search.search_plate(db=db, tipo=6)
        suco = search.search_plate(db=db, tipo=7)

        lista_refeicoes.append(acomp_arroz)
        lista_refeicoes.append(acomp_feijao)
        lista_refeicoes.append(entrada)
        lista_refeicoes.append(guarnicao)
        lista_refeicoes.append(principal)
        lista_refeicoes.append(sobremesa)
        lista_refeicoes.append(suco)


    elif refeicao == 3:
        fruta = search.search_plate(db=db, tipo=8)
        bebida = search.search_plate(db=db, tipo=7)
        pao_cereal = search.search_plate(db=db, tipo=8)

        lista_refeicoes.append(fruta)
        lista_refeicoes.append(bebida)
        lista_refeicoes.append(pao_cereal)

    else:
        return "Nao existe o tipo de refeicao desejado!"
        
    return lista_refeicoes


def plate_random_desjejum(db: Session):

    prato_desjejum = []

    pratos_desjejum = generate_plate(1, db=db)

    for i in range(len(pratos_desjejum)):
        tam = len(pratos_desjejum[i])
        aux = randint(0, tam-1)

        prato_desjejum.append(pratos_desjejum[i][aux])

    return prato_desjejum


def plate_random_almoco(db: Session):

    prato_almoco = []

    pratos_almoco = generate_plate(2, db=db)

    for i in range(len(pratos_almoco)):
        tam = len(pratos_almoco[i])
        aux = randint(0, tam-1)

        prato_almoco.append(pratos_almoco[i][aux])

    return prato_almoco


def plate_random_lanche(db: Session):

    prato_lanche = []

    pratos_lanche = generate_plate(3, db=db)

    for i in range(len(pratos_lanche)):
        tam = len(pratos_lanche[i])
        aux = randint(0, tam-1)

        prato_lanche.append(pratos_lanche[i][aux])
    
    return prato_lanche