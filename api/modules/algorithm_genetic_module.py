from api.modules.menu_module import generate_menu_pop
from api.modules.food_module import plates
from api.model import crud, models, schemas, search
from sqlalchemy.orm import Session
import random
from api.model.search import search_food, search_plate


def generate_population(tam_pop, db: Session):
    populacao = []

    for i in range(tam_pop):
        individuo = generate_menu_pop(db=db)
        populacao.append(individuo)

    return populacao


def function_soma(cardapio_dia, db: Session):
    nutrientes = {"Energia": 0, "CHO": 0, "PTN": 0, "LIP": 0, "Fibras": 0, "Ca": 0, "Fe": 0, "Mg": 0, "Zn": 0}
    soma_valores_almoco = 0
    soma_valores_desjejum = 0
    soma_valores_lanche = 0

    almoco = cardapio_dia['almoco']

    for prato in almoco:
        alimentos_pratos = plates(prato, db=db)

        if prato.tipo == 1:
            qtd_prato = 50
        elif prato.tipo == 2:
            qtd_prato = 35
        elif prato.tipo == 3:
            qtd_prato = 30
        elif prato.tipo == 4:
            qtd_prato = 25
        elif prato.tipo == 5:
            qtd_prato = 120
        elif prato.tipo == 6:
            qtd_prato = 120
        elif prato.tipo == 7:
            qtd_prato = 150
        else:
            qtd_prato = 20

        for alimento in alimentos_pratos:
            nutrientes['Energia'] += int(alimento[0].energia) * qtd_prato
            nutrientes['CHO'] += alimento[0].proteinas * qtd_prato
            nutrientes['PTN'] += alimento[0].carboidratos * qtd_prato
            nutrientes['LIP'] += alimento[0].lipideos * qtd_prato
            nutrientes['Fibras'] += alimento[0].fibras * qtd_prato
            nutrientes['Ca'] += int(alimento[0].calcio) * qtd_prato
            nutrientes['Fe'] += alimento[0].ferro * qtd_prato
            nutrientes['Mg'] += alimento[0].zinco * qtd_prato
            nutrientes['Zn'] += alimento[0].magnesio * qtd_prato
            soma_valores_almoco += (alimento[0].valor * qtd_prato) / 1000

    desjejum = cardapio_dia['desjejum']

    i = 0

    for alimento in desjejum:
        if i == 0:
            qtd_prato = 120
        elif i == 1:
            qtd_prato = 150
        else:
            qtd_prato = 200

        nutrientes['Energia'] += int(alimento.energia) * qtd_prato
        nutrientes['CHO'] += alimento.proteinas * qtd_prato
        nutrientes['PTN'] += alimento.carboidratos * qtd_prato
        nutrientes['LIP'] += alimento.lipideos * qtd_prato
        nutrientes['Fibras'] += alimento.fibras * qtd_prato
        nutrientes['Ca'] += int(alimento.calcio) * qtd_prato
        nutrientes['Fe'] += alimento.ferro * qtd_prato
        nutrientes['Mg'] += alimento.zinco * qtd_prato
        nutrientes['Zn'] += alimento.magnesio * qtd_prato
        soma_valores_desjejum += (alimento.valor * qtd_prato) / 1000

        i += 1

    lanche = cardapio_dia['lanche']

    i = 0

    for alimento in lanche:
        if i == 0:
            qtd_prato = 120
        elif i == 1:
            qtd_prato = 150
        else:
            qtd_prato = 200

        nutrientes['Energia'] += int(alimento.energia) * qtd_prato
        nutrientes['CHO'] += alimento.proteinas * qtd_prato
        nutrientes['PTN'] += alimento.carboidratos * qtd_prato
        nutrientes['LIP'] += alimento.lipideos * qtd_prato
        nutrientes['Fibras'] += alimento.fibras * qtd_prato
        nutrientes['Ca'] += int(alimento.calcio) * qtd_prato
        nutrientes['Fe'] += alimento.ferro * qtd_prato
        nutrientes['Mg'] += alimento.zinco * qtd_prato
        nutrientes['Zn'] += alimento.magnesio * qtd_prato
        soma_valores_lanche += (alimento.valor * qtd_prato) / 1000

        i += 1

    card_dia = {
        "nutrientes": nutrientes,
        "soma_desjejum": soma_valores_desjejum,
        "soma_almoco": soma_valores_almoco,
        "soma_lanche": soma_valores_lanche
    }

    return card_dia


def function_fitness(populacao, db: Session):
    nova_populacao = []

    referencia_nutricional = {"Energia": 1305, "CHO": 212.1, "PTN": 40.8, "LIP": 32.7, "Fibras": 18.3, "Ca": 780,
                              "Fe": 6.3, "Mg": 189, "Zn": 5.4}

    qtd_ind = 0

    for individuo in populacao:
        somas = function_soma(individuo, db=db)

        nutrientes = somas["nutrientes"]
        flag = 0

        for i in referencia_nutricional:
            if referencia_nutricional[i] > nutrientes[i]:
                flag += 1

        if flag > 4:
            if somas['soma_desjejum'] < 3 and somas['soma_almoco'] < 6 and somas['soma_lanche'] < 3:
                qtd_ind += 1
                for _ in range(flag):
                    nova_populacao.append(individuo)

    return nova_populacao, qtd_ind


def function_selection(nova_populacao, qtd_ind):
    if qtd_ind == 1:
        selecionados = nova_populacao[0]
    else:
        tamanho = qtd_ind
        tamanho_nova_pop = len(nova_populacao)
        quantidade_selecao = int(tamanho / 2)
        selecionados = list()

        while len(selecionados) < quantidade_selecao:
            aleatorio = random.randint(0, tamanho_nova_pop - 1)
            pop = nova_populacao[aleatorio]

            if pop not in selecionados:
                selecionados.append(pop)

    return selecionados


def crossover(selecionados):
    cruzados = []
    tamanho = len(selecionados)

    if tamanho > 1:
        for i in range(tamanho - 1):
            ponto_corte = random.randint(0, 2)
            pai = selecionados[i]
            mae = selecionados[i + 1]

            desjejum1 = pai['desjejum']
            desjejum2 = mae['desjejum']

            almoco1 = pai['almoco']
            almoco2 = mae['almoco']

            lanche1 = pai['lanche']
            lanche2 = mae['lanche']

            new_desjejum1 = [desjejum1[0:ponto_corte], desjejum2[ponto_corte:]]
            new_desjejum2 = [desjejum1[ponto_corte:], desjejum2[0:ponto_corte]]

            new_lanche1 = [lanche1[0:ponto_corte], lanche2[ponto_corte:]]
            new_lanche2 = [lanche1[ponto_corte:], lanche2[0:ponto_corte]]

            ponto_corte = random.randint(0, 6)

            new_almoco1 = [almoco1[0:ponto_corte], almoco2[ponto_corte:]]
            new_almoco2 = [almoco1[ponto_corte:], almoco2[0:ponto_corte]]

            metade_filho = {"desjejum": new_desjejum1, "almoco": new_almoco1, "lanche": new_lanche1}
            outra_metade_filho = {"desjejum": new_desjejum2, "almoco": new_almoco2, "lanche": new_lanche2}

            cruzados.append(metade_filho)
            cruzados.append(outra_metade_filho)
    else:
        cruzados.append(selecionados[0])

    return cruzados


def mutation(crossed, db: Session):
    mutados = []

    for ind in crossed:
        posicao = random.randint(0, 2)

        if posicao == 0:
            new = search_food(db=db, grupo=3)
        elif posicao == 1:
            new = search_food(db=db, grupo=7)
        else:
            new = search_food(db=db, grupo=1)

        ind['desjejum'][posicao] = new

        posicao = random.randint(0, 2)

        if posicao == 0:
            new = search_food(db=db, grupo=3)
        elif posicao == 1:
            new = search_food(db=db, grupo=8)
        else:
            new = search_food(db=db, grupo=1)

        ind['lanche'][posicao] = new

        posicao = random.randint(1, 7)

        new = search_plate(db=db, tipo=posicao)

        ind['almoco'][posicao - 1] = new

        mutados.append(ind)

    return mutados
