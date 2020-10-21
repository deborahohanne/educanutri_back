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

    tam_frutas = len(pratos_desjejum[0])
    tam_leite_der = len(pratos_desjejum[1])
    tam_pao_cer = len(pratos_desjejum[2])

    aux1 = randint(0, tam_frutas-1)
    aux2 = randint(0, tam_leite_der-1)
    aux3 = randint(0, tam_pao_cer-1)

    prato_desjejum.append(pratos_desjejum[0][aux1])
    prato_desjejum.append(pratos_desjejum[1][aux2])
    prato_desjejum.append(pratos_desjejum[2][aux3])

    return prato_desjejum


def plate_random_almoco(db: Session):

    prato_almoco = []

    pratos_almoco = generate_plate(2, db=db)

    tam_acomp_arroz = len(pratos_almoco[0])
    tam_acomp_feijao = len(pratos_almoco[1])
    tam_entrada = len(pratos_almoco[2])
    tam_guarnicao = len(pratos_almoco[3])
    tam_principal = len(pratos_almoco[4])
    tam_sobremesa = len(pratos_almoco[5])
    tam_suco = len(pratos_almoco[6])

    aux1 = randint(0, tam_acomp_arroz-1)
    aux2 = randint(0, tam_acomp_feijao-1)
    aux3 = randint(0, tam_entrada-1)
    aux4 = randint(0, tam_guarnicao-1)
    aux5 = randint(0, tam_principal-1)
    aux6 = randint(0, tam_sobremesa-1)
    aux7 = randint(0, tam_suco-1)

    prato_almoco.append(pratos_almoco[0][aux1])
    prato_almoco.append(pratos_almoco[1][aux2])
    prato_almoco.append(pratos_almoco[2][aux3])
    prato_almoco.append(pratos_almoco[3][aux4])
    prato_almoco.append(pratos_almoco[4][aux5])
    prato_almoco.append(pratos_almoco[5][aux6])
    prato_almoco.append(pratos_almoco[6][aux7])

    return prato_almoco


def plate_random_lanche(db: Session):

    prato_lanche = []

    pratos_lanche = generate_plate(3, db=db)

    tam_frutas = len(pratos_lanche[0])
    tam_bebidas = len(pratos_lanche[1])
    tam_pao_cer = len(pratos_lanche[2])

    aux1 = randint(0, tam_frutas-1)
    aux2 = randint(0, tam_bebidas-1)
    aux3 = randint(0, tam_pao_cer-1)

    prato_lanche.append(pratos_lanche[0][aux1])
    prato_lanche.append(pratos_lanche[1][aux2])
    prato_lanche.append(pratos_lanche[2][aux3])
    
    return prato_lanche