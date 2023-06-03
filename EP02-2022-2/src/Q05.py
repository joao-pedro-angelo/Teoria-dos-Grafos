import networkx as nx


def change_costs_factor(ddc, c):
    
    #Verificação da validade dos parâmetros
    if (not verificaParametros(ddc, c)):
        return None
      
    #Retorna o cálculo do fator resultado, incrementado em uma unidade. Pois cada classe tem custo 1
    return (calculaFatorResultante(ddc, c) + 1)


#Calcula o fator resultante 
def calculaFatorResultante(ddc, c):
    fator_resultante = 0
    
    #Para cada vértice que pode ser alcançado a partir de c, incrementado o fator em 1 unidade
    for vertice in list(ddc.nodes): 
        if(vertice != c):
            if (len(list(nx.all_simple_paths(ddc, vertice, c))) > 0):
                fator_resultante += 1
            
    #Para cada componente forte, de tamanho maior que 3, incrementamos o fator em 50 unidades
    sets_tangles = nx.strongly_connected_components(ddc)
    for set in sets_tangles:
        if(c in set):
            if (len(set) > 3):
                fator_resultante += 50
            
    #Para cada ciclo em que c está presente, incrementamos o fator em 10 unidades
    ciclos = nx.simple_cycles(ddc)
    for ciclo in ciclos:
        if(c in ciclo):
            fator_resultante += 10
    
    return fator_resultante


#Verificação de parâmetros
def verificaParametros(ddc, c):
    result = True
    
    #Verifica se o grafo é vazio
    if(ddc is None):
        result = False
        
    #Verifica se o vértice é vazio
    elif (c is None):
        result = False
    
    #Verifica se o grafo é direcionado
    elif (not nx.is_directed(ddc)):
        result = False
        
    #Verifica se c está no grafo
    elif (c not in ddc.nodes):
        result = False
        
    return result
