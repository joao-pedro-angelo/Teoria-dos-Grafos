import networkx as nx


def graph_density(g):
    #Verifica se o grafo é inválido
    if (g is None):
        return None
    
    #Armazena os números de vértices e arestas
    num_vertices = g.number_of_nodes()
    num_arestas = g.number_of_edges()

    #Verifica se é um grafo trivial ou nulo
    if num_arestas == 0 or num_vertices <= 1:
        return 0
    
    #Funções para testar se o grafo tem multiplas arestas, se é pseudografo e se é multigrafo
    has_multiple_edges = lambda g: (any(g.number_of_edges(u, v) > 1 for u in g.nodes for v in g.nodes))
    is_pseudograph = lambda g: nx.number_of_selfloops(g) > 0
    is_multigraph = lambda g: not is_pseudograph(g) and has_multiple_edges(g)
    
    #Caso ele seja multigrafo ou pseudografo retorna None, senão faz o cálculo da densidade e retorna o mesmo
    if is_multigraph(g) or is_pseudograph(g):
        return None
    else:
        return round(nx.density(g), 2)
    
