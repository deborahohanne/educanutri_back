from sqlalchemy.orm import Session
from api.model import crud, models, schemas, search
from api.model.database import SessionLocal
from api.modules.plate_module import plate_random_desjejum, plate_random_almoco, plate_random_lanche

from random import randint


def generate_menu(db: Session):
    prato_desjejum = plate_random_desjejum(db=db)
    prato_almoco = plate_random_almoco(db=db)
    prato_lanche = plate_random_lanche(db=db)

    cardapio_dia_dict = {"desjejum": prato_desjejum, "almoco": prato_almoco, "lanche": prato_lanche}

    return cardapio_dia_dict


def generate_menu_pop(db: Session):
    cardapio = generate_menu(db=db)

    return cardapio
