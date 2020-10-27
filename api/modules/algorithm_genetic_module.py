from api.modules.menu_module import generate_menu_week
from api.modules.food_module import plates, card
from api.model import crud, models, schemas, search
from sqlalchemy.orm import Session


 
def generate_population(tam_pop, db: Session):

    populacao = []

    for i in range(tam_pop):
        individuo = generate_menu_week(db=db)
        populacao.append(individuo)

    return populacao


def function_soma(individuo, db: Session):
    soma = []
    almoco_dia = []
    soma_valores = 0
    soma_nutrientes = 0

    for i in range(len(individuo)):
        cardapio_dia = individuo[i]
        for k in range(len(cardapio_dia)):
            cardapio = cardapio_dia['almoco']
            for j in range(len(cardapio)):
                alimentos_pratos = plates(cardapio[j], db=db)
                for l in range(len(alimentos_pratos))   :
                    for m in range(len(alimentos_pratos[l])):
                        soma_nutrientes = alimentos_pratos[l][m].energia + alimentos_pratos[l][m].proteinas + alimentos_pratos[l][m].carboidratos + alimentos_pratos[l][m].lipideos + alimentos_pratos[l][m].fibras + alimentos_pratos[l][m].calcio + alimentos_pratos[l][m].ferro + alimentos_pratos[l][m].zinco + alimentos_pratos[l][m].magnesio 
                        soma_valores += alimentos_pratos[l][m].valor                   



def function_nutritional_error(populacao, db: Session):


    pass


def function_custo(populacao, db: Session):

    pass

def function_fitness(populacao, db: Session):
    
    pass