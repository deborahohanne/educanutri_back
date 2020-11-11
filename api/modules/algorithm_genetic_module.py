from api.modules.menu_module import generate_menu_week
from api.modules.food_module import plates
from api.model import crud, models, schemas, search
from sqlalchemy.orm import Session
import random

 
def generate_population(tam_pop, db: Session):

    populacao = []

    for i in range(tam_pop):
        individuo = generate_menu_week(db=db)
        populacao.append(individuo)

    return populacao


def function_soma(individuo, db: Session):
    card_dia = []


    for cardapio_dia in individuo:
        nutrientes = {"Energia": 0, "CHO": 0, "PTN": 0, "LIP": 0, "Fibras": 0, "Ca": 0, "Fe": 0, "Mg": 0, "Zn": 0}
        soma_valores = 0
        almoco = cardapio_dia['almoco']
        

        for prato in almoco:
            alimentos_pratos = plates(prato, db=db)

            for alimento in alimentos_pratos:
                nutrientes['Energia'] += int(alimento[0].energia) 
                nutrientes['CHO'] += alimento[0].proteinas 
                nutrientes['PTN'] += alimento[0].carboidratos 
                nutrientes['LIP'] += alimento[0].lipideos 
                nutrientes['Fibras'] += alimento[0].fibras 
                nutrientes['Ca'] += int(alimento[0].calcio) 
                nutrientes['Fe'] += alimento[0].ferro 
                nutrientes['Mg'] += alimento[0].zinco
                nutrientes['Zn'] += alimento[0].magnesio 
                soma_valores += alimento[0].valor   
        
        
        desjejum = cardapio_dia['desjejum']

        for alimento in desjejum:
            nutrientes['Energia'] += int(alimento.energia) 
            nutrientes['CHO'] += alimento.proteinas 
            nutrientes['PTN'] += alimento.carboidratos 
            nutrientes['LIP'] += alimento.lipideos 
            nutrientes['Fibras'] += alimento.fibras 
            nutrientes['Ca'] += int(alimento.calcio) 
            nutrientes['Fe'] += alimento.ferro 
            nutrientes['Mg'] += alimento.zinco
            nutrientes['Zn'] += alimento.magnesio 
            soma_valores += alimento.valor    


        lanche = cardapio_dia['lanche']

        for alimento in lanche:
            nutrientes['Energia'] += int(alimento.energia) 
            nutrientes['CHO'] += alimento.proteinas 
            nutrientes['PTN'] += alimento.carboidratos 
            nutrientes['LIP'] += alimento.lipideos 
            nutrientes['Fibras'] += alimento.fibras 
            nutrientes['Ca'] += int(alimento.calcio) 
            nutrientes['Fe'] += alimento.ferro 
            nutrientes['Mg'] += alimento.zinco
            nutrientes['Zn'] += alimento.magnesio 
            soma_valores += alimento.valor    


        card_dia.append([nutrientes, soma_valores])


    return card_dia


def function_fitness(valor_cliente, populacao, db: Session):
    nova_populacao = []
    valores_refeicoes = []
    valor_aceito = []

    
    referenia_nutricional = {"Energia": 1305, "CHO": 212.1, "PTN": 40.8, "LIP": 32.7, "Fibras": 18.3, "Ca": 780, "Fe": 6.3, "Mg": 189, "Zn": 5.4}

    for individuo in populacao:
        somas = function_soma(individuo, db=db)
        valor_aceito = []

        for soma in somas:
            if soma[1] <= valor_cliente:
                valor_aceito.append(soma[1]) 

        if len(valor_aceito) >= 3:
            nova_populacao.append(individuo)     

    return nova_populacao


def function_selection(nova_populacao):

    tamanho = len(nova_populacao)
    quantidade_selecao = int(tamanho/2)
    selecionados = list()


    while(len(selecionados) < quantidade_selecao):
        aleatorio = random.randint(0, tamanho-1)
        pop = nova_populacao[aleatorio]

        if pop not in selecionados:
            selecionados.append(pop)
        
    return selecionados


def crossover(selecionados):

    cruzados = []
    tamanho = len(selecionados)

    if tamanho > 1:
        for i in range(tamanho-1):
            ponto_corte = random.randint(0, 5)
            pai  = selecionados[i]
            mae = selecionados[i+1]

            metade_filho = []
            outra_metade_filho = []

            metade_filho.append(pai[0:ponto_corte])
            metade_filho.append(mae[ponto_corte:])

            outra_metade_filho.append(pai[ponto_corte:])
            outra_metade_filho.append(mae[0:ponto_corte])

            cruzados.append(metade_filho)
            cruzados.append(outra_metade_filho)

            return cruzados
    else:
        return selecionados
