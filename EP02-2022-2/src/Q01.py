import networkx as nx


#ddc --> grafo direcionado
#c --> vértice do grafo ddc
def class_metrics(ddc, c):
    
    #Verifica se os parâmetros são válidos
    if (not verificaParametros(ddc, c)):
        return None
    
    #Calcula o grau de entrada do vértice c
    fan_in = ddc.in_degree(c)
    
    #Calcula o grau de saída do vértice c
    fan_out = ddc.out_degree(c)
    return (fan_out, fan_in)


def verificaParametros(ddc, c):
    
    result = True
    
    #Verifica se o grafo é vazio
    if (ddc is None):
        result = False
        
    #Verifica se o grafo é direcionado
    elif (not ddc.is_directed()):
        result = False
        
    #Verifica se o vértice é vazio
    elif (c is None):
        result = False
        
    #Verifica se o vértice está no grafo
    elif (not ddc.__contains__(c)):
        result = False
        
    #Verifica se o grafo tem vértices
    elif (ddc.order() == 0):
        result = False
        
    return result