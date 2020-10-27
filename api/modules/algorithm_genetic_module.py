from api.modules.menu_module import generate_menu_week
from api.modules.food_module import plates, card
from api.model import crud, models, schemas, search
from sqlalchemy.orm import Session



def generate_population(tam_pop, db: Session):

    populacao = []

    for i in range(tam_pop):
        individuo = []
        cardapios_semana = generate_menu_week(db=db)
        individuo.append(cardapios_semana)

        populacao.append(individuo)

    return populacao


def function_nutritional_error(populacao, db: Session):

    para_fitness = plates(populacao, db=db)

    pratos = plates(populacao, db=db)

    cards = card(pratos_dia=pratos, db=db)

    return cards

def function_custo(populacao, db: Session):

    pass

def function_fitness(populacao, db: Session):
    
    pass