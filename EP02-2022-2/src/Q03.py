import networkx as nx

#ddc --> grafo direcionado
#c --> vértice que deve estar em ddc
def dependencies(ddc, c):
    
    #Verifica a validade dos parâmetros
    if (not verificaParametros(ddc, c)):
        return None
    
    #Itera pelos vértices do grafo, verificando se o vértice que está sendo iterado é
    #alcançavel a partir de v, que é o vértice recebido como parâmetro
    v = c
    reachable = []
    not_reachable = []
    for u in ddc.nodes:
        if not v == u: 
            try:
                paths = nx.shortest_simple_paths(ddc,v,u)
                p = next(paths) # se não existir, lança exceção NetworkXNoPath
                
                #Se for alcançavel
                reachable.append(u)
            except nx.NetworkXNoPath:
                #Se não for alcançavel
                not_reachable.append(u)
    
    #Após termos a lista de vértices alcancáveis a partir de c, vamos verificar quais são
    #Diretamente ligados a c e quais são indiretamente ligados
    direta = []
    indireta = []
    for w in reachable:
        
        #Se tiver aresta entre c e w, então é diretamente ligado
        if (ddc.has_edge(c, w)):
            direta.append(w)
        else:
            indireta.append(w)
    
    #Caso exista um loop em c, então este vértice é diretamente ligado com ele mesmo
    if (ddc.has_edge(c, c)):
        direta.append(c)
        
    return direta, indireta


def verificaParametros(ddc, c):
    
    #Falta verificar se o grafo é direcionado

    result = True
    
    #Caso ddc for None
    if (ddc is None):
        result = False
    
    #Caso o grafo não seja direcionado
    elif (not ddc.is_directed()):
        result = False
        
    #Caso c for None
    elif (c is None):
        result = False
        
    #Caso c não esteja em ddc
    elif (not ddc.__contains__(c)):
        result = False
        
    #Caso ddc não tenha vértices
    elif (ddc.order() == 0):
        result = False
        
    return result
    