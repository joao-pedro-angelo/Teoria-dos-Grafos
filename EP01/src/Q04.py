import networkx as nx

def best_route(G, i):

    # Verifica se o grafo ou vertice não são None ou se o vertice inicial é 1
    if G is None or i is None or i == 1:
        return None

    # Verifica se o vértice está no grafo
    if not G.has_node(i):
        return None
    # Verificação se o vértice já está cheio (se estiver não pode ser estar incluso na lista de vértices)
    # Lista onde ficarão armazenados os vértices a serem retornados
    if (G.nodes[i]['full']):
        lista_vertices = []
    else:
        lista_vertices = [i]
    vertice_atual = i

    while True:
        # Adiciona numa lista os vizinhos do vertice atual que satisfazem as condições
        lista_vizinhos = []
        for v in G.neighbors(vertice_atual):
            if G.nodes[v]['depth'] is None or G.nodes[v]['full'] is None:
                return None
            elif not G.nodes[v]['full'] and G.nodes[v]['depth'] > G.nodes[vertice_atual]['depth'] and not G.nodes[vertice_atual]['full']:
                lista_vizinhos.append(v)

        # Caso não tenha mais vizinhos ou vizinhos válidos o vertice será o armazenamento final do alimento
        if not lista_vizinhos:
            break

        # Seleciona o vertice que tem a menor profundidade e insere ele na lista de vértices
        proximo_vertice = min(lista_vizinhos, key=lambda n: G.nodes[n]['depth'])
        lista_vertices.append(proximo_vertice)

        # Atualiza o vertice atual
        vertice_atual = proximo_vertice

    return lista_vertices