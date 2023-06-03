import networkx as nx
from src.Q04 import mfs_greedy



def class_order(ddc):
    
    #Verifica se os parâmetros são válidos
    if  (not verifica_parametros(ddc)):
        return None
    
    #Caso o grafo seja acíclico
    if (nx.is_directed_acyclic_graph(ddc)):
        return gera_ordem_topologica(ddc)
    
    #Caso o grafo tenha ciclo
    else:
        #Calcula o msf
        mfs = mfs_greedy(ddc)
        
        #Retira os arcos presentes no msf
        for arco in mfs:
            ddc.remove_edge(arco[0], arco[1])
        
        return gera_ordem_topologica(ddc)
    

#Verificação dos parâmetros
def verifica_parametros(ddc):
    result = True
    
    if (ddc is None):
        result = False
    elif (not ddc.is_directed()):
        result = False
    
    return result


#Cálculo da ordem topológica
def gera_ordem_topologica(ddc):
    generation = [(generation) for generation in nx.topological_generations(ddc)]
        
    result = []
    for lista in generation[::-1]:
        result.append(lista)
    return result