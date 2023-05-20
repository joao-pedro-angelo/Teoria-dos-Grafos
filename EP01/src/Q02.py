import networkx as nx

def is_candidate(g, q_list, q, t):
   #Verifica se algum parâmetro é nulo ou inválido:
    parametros_validos = testa_parametros(g, q_list, q, t)
    if (not parametros_validos):
        return None
    
    #Verificando se há como chegar no vértice q a partir de algum vértice de q_list
    tem_conexao = False
    for vertice in q_list:
        if g.has_edge(q, vertice):
            tem_conexao = True
    if not tem_conexao:
        return False
    
    #Itera sobre os nós da lista, verificando se o menor caminho entre cada nó da lista e o 
    #nó 'q', é maior que o limite. Se for, retorna False.
    for node in q_list:
        paths_w = nx.shortest_simple_paths(g, node, q, weight='weight')
        W = next(paths_w)
        Peso = sum([g[W[i]][W[i+1]]['weight'] for i in range(len(W)-1)])
        if (Peso > t):
            return False
    return True


def testa_parametros(g, q_list, q, t):
    #Verifica se algum parâmetro é vazio
    if (g is None or q_list is None or q is None or t is None):
      return False
    
    #Verifica se o vértice q está na lista ou se a distância "t" é menor que 0
    if (q in q_list or t < 0):
        return False
    
    #Verifica se o vértice q está no grafo g
    if (not g.__contains__(q)):
        return False
    
    #Verifica se algum vértice da lista não está presente no grafo
    for vertice in q_list:
        if (not g.__contains__(vertice)):
            return False

    return True