from sqlalchemy.orm import Session
from api.model import crud, models, schemas, search
from api.model.database import SessionLocal
from api.modules.plate_module import plate_random_desjejum, plate_random_almoco, plate_random_lanche

from random import randint


def generate_menu(db: Session):

    cardapio_dia_lista = []

    prato_desjejum = plate_random_desjejum(db=db)
    prato_almoco = plate_random_almoco(db=db)
    prato_lanche = plate_random_lanche(db=db)

    cardapio_dia_lista.append(prato_desjejum)
    cardapio_dia_lista.append(prato_almoco)
    cardapio_dia_lista.append(prato_lanche)

    cardapio_dia_dict = {"desjejum": prato_desjejum, "almoco": prato_almoco, "lanche": prato_lanche}

    return cardapio_dia_dict


def generate_menu_week(db: Session):

    cardapio = {}
    cardapios_semana = []

    for i in range(5):
        cardapio = generate_menu(db=db)
        cardapios_semana.append(cardapio)

    return cardapios_semana