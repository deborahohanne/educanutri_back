from api.modules.menu_module import generate_menu_week
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