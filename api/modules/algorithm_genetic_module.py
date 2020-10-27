from api.modules.menu_module import generate_menu_week
from api.modules.food_module import plates
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
    nutrientes = {"Energia": 0, "CHO": 0, "PTN": 0, "LIP": 0, "Fibras": 0, "Ca": 0, "Fe": 0, "Mg": 0, "Zn": 0 }


    for cardapio_dia in individuo:
        almoco = cardapio_dia['almoco']

        for prato in almoco:
            alimentos_pratos = plates(prato, db=db)

            for alimento in alimentos_pratos:
                nutrientes['Energia'] = alimento[0].energia 
                nutrientes['CHO'] = alimento[0].proteinas 
                nutrientes['PTN'] = alimento[0].carboidratos 
                nutrientes['LIP'] = alimento[0].lipideos 
                nutrientes['Fibras'] = alimento[0].fibras 
                nutrientes['Ca'] = alimento[0].calcio 
                nutrientes['Fe'] = alimento[0].ferro 
                nutrientes['Mg'] = alimento[0].zinco
                nutrientes['Zn'] = alimento[0].magnesio 
                soma_valores += alimento[0].valor   
        
        
        desjejum = cardapio_dia['desjejum']

        for alimento in desjejum:
            nutrientes['Energia'] = alimento.energia 
            nutrientes['CHO'] = alimento.proteinas 
            nutrientes['PTN'] = alimento.carboidratos 
            nutrientes['LIP'] = alimento.lipideos 
            nutrientes['Fibras'] = alimento.fibras 
            nutrientes['Ca'] = alimento.calcio 
            nutrientes['Fe'] = alimento.ferro 
            nutrientes['Mg'] = alimento.zinco
            nutrientes['Zn'] = alimento.magnesio 
            soma_valores += alimento.valor    


        lanche = cardapio_dia['lanche']

        for alimento in lanche:
            nutrientes['Energia'] = alimento.energia 
            nutrientes['CHO'] = alimento.proteinas 
            nutrientes['PTN'] = alimento.carboidratos 
            nutrientes['LIP'] = alimento.lipideos 
            nutrientes['Fibras'] = alimento.fibras 
            nutrientes['Ca'] = alimento.calcio 
            nutrientes['Fe'] = alimento.ferro 
            nutrientes['Mg'] = alimento.zinco
            nutrientes['Zn'] = alimento.magnesio 
            soma_valores += alimento.valor    


        almoco_dia.append([nutrientes, soma_valores])


    return almoco_dia


def function_nutritional_error(populacao, db: Session):

    pass


def function_custo(populacao, db: Session):

    pass

def function_fitness(populacao, db: Session):
    
    pass