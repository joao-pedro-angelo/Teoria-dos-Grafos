import networkx as nx
from src.Q01 import class_metrics


def silent_villains(ddc, threshold):

    # Verificação de parâmetros válidos.

    if (not verificaParametros(ddc, threshold)):
        return None
    
    # Lista que representa as classes que tem dependência excessiva de outras, considerando o limite threshold.
    breakable = []

    # Lista que representa as classes que tem possuem muitos dependentes, considerando o limite threshold.
    butterfly = []

    # Lista que representa as classes que possuem tanto breakable tanto butterfly.
    hub = []

    # Passagem por cada classe do grafo orientado , atribuindo os graus de dependências e dependentes.
    for c in ddc.nodes:
        fan_out, fan_in = class_metrics(ddc, c)
       

    # Aplicação de condicionais que irão classificar a classe em butterfly, breakable e hub.
        if (fan_in > threshold):
            butterfly.append(c)
        if (fan_out > threshold):
            breakable.append(c)
        if (fan_in > threshold and fan_out > threshold):
            hub.append(c)
    return breakable, butterfly, hub


def verificaParametros(ddc, threshold):

    # Verifica se são parâmetros válidos.

    result = True
    if (ddc is None):
        result = False
    elif (not ddc.is_directed()):
        result = False
    elif (threshold is None):
        result = False
    elif (threshold < 0):
        result = False

    return result
