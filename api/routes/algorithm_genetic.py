from fastapi import FastAPI, APIRouter, Depends
from api.modules.menu_module import generate_menu
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

    card_dia_lista, card_dia_dict = generate_menu(db=db)

    result = card_dia_dict

    return {"resultado": result}
