from sqlalchemy.orm import Session
from api.model import crud, models, schemas, search
from api.model.database import SessionLocal
 


def plates(populacao, db: Session):

    tam_pop = len(populacao)
    pratos_dia = []
    pratos = []

    for i in range(tam_pop):
        individuo = populacao[i]
        for j in range(len(individuo)):
            cardapio_semana = populacao[i][j]
            for k in range(len(cardapio_semana)):
                cardapio_dia = cardapio_semana[k]
                pratos_dia.append(cardapio_dia['desjejum'])
                pratos_dia.append(cardapio_dia['almoco'])
                pratos_dia.append(cardapio_dia['lanche'])

                pratos.append(pratos_dia)

    return pratos


def card(pratos_dia, db: Session): 

    pratos_alimentos_lis = []
    card = []
    alimentos_almoco = []
    

    for i in range(len(pratos_dia)):
        for j in range(len(pratos_dia[i])):
            for k in range(len(pratos_dia[i][j])):
                id_prato = pratos_dia[i][j][k].id
                pratos_alimentos_lis.append(search.search_creation(db=db, id_prato=id_prato))
                
                for e in range(len(pratos_alimentos_lis)):
                    for f in range(len(pratos_alimentos_lis[e])):
                        id_alimento = pratos_alimentos_lis[e][f].id_alimento
                        alimentos_almoco.append(search.search_foods(db=db, id_alimento=id_alimento))
    
                        card.append(pratos_dia[0])
                        card.append(alimentos_almoco)
                        card.append(pratos_dia[2])

    return card
