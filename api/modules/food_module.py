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
