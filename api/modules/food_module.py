from sqlalchemy.orm import Session
from api.model import crud, models, schemas
from api.model.search import search_foods, search_creation
from api.model.database import SessionLocal
 


def plates(almoco, db: Session):

    alimentos = search_creation(db=db, id_prato=almoco.id)
    alimentos_prato = []

    for i in range(len(alimentos)):
        alimentos_prato.append(search_foods(db=db, id_alimento=alimentos[i].id_alimento))

    return alimentos_prato


def card(pratos_dia, db: Session): 

    '''
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
    '''
    return card
