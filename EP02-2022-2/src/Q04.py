import networkx as nx
from src.Q01 import class_metrics


# Função que retorna uma lista de arcos contendo um conjunto mínimo de depedências
# Recebe um grafo direcionado como parametro
def mfs_greedy(ddc):

    if(not verifica_parametros(ddc)):
        return None

    md_cycles = find_mdc(ddc)
    mfs = []

    while (md_cycles):
        cont_max_ocorrences = 0
        arc_max = None

        for cycle in md_cycles:

            for arc in cycle:
                cont_ocorrences = 0

                for c in md_cycles:
                    if(arc in c):
                        cont_ocorrences += 1

                if(cont_max_ocorrences < cont_ocorrences or (desempatar(ddc, arc, arc_max) and cont_max_ocorrences == cont_ocorrences)):
                    arc_max = arc
                    cont_max_ocorrences = cont_ocorrences

        mfs.append(arc_max)

        lista_aux = []
        for cycle in md_cycles:
            if(arc_max not in cycle):
                lista_aux.append(cycle)
        md_cycles = lista_aux

    return mfs


# Função para verificar se o grafo recebido é válido
def verifica_parametros(ddc):
    retorno = True

    # Verifica se o grafo é None
    if(ddc is None):
        retorno = False

    # Verifica se ele não é direcionado
    elif(not ddc.is_directed()):
        retorno = False

    return retorno


# Função para encontrar os ciclos de dependência mínimos
# Recebe um grafo direcionado como parâmetro
def find_mdc(ddc):
    list_cycles = []
    list_arcs = []
    painted = set()

    # Realizada a busca em profundidade em cada vértice do grafo
    for v in ddc:
        if (v not in painted):
            busca_em_profundidade([], v, painted, list_cycles, ddc)

    for cycle in list_cycles:
        if(len(set(cycle)) == len(cycle) and len(cycle) < len(ddc)):

            list_aux_arc = []
            for i in range(len(cycle) - 1):
                arc = (cycle[i], cycle[i+1])
                list_aux_arc.append(arc)

            list_aux_arc.append((cycle[-1], cycle[0]))
            list_arcs.append(list_aux_arc)

    return list_arcs


# Algoritmo da busca em profunidade
# Recebe como parametros o caminho, o vértice, e os vértices que já foram "pintados", ou seja, já foram visitados
# Além do grafo e da lista de ciclos, que também são parâmetros.
def busca_em_profundidade(path, vertice, painted, list_cycles, ddc):
    path.append(vertice)
    painted.add(vertice)

    for neighbor in ddc[vertice]:
        if (neighbor in path):
            position = path.index(neighbor)
            cycle = path[position:]

            if (cycle not in list_cycles):
                list_cycles.append(cycle)

        elif (neighbor not in painted):
            busca_em_profundidade(path, neighbor, painted, list_cycles, ddc)

    painted.remove(vertice)
    path.pop()


# Função para escolher um arco em caso de empate
# Recebe como parametros um grafo direcionado e dois arcos
def desempatar(ddc, arc_x, arc_y):
    
    fan_out_x, fan_in_x = class_metrics(ddc, arc_x[0])
    fan_out_y, fan_in_y = class_metrics(ddc, arc_y[0])

    result = False

    if (fan_out_x > fan_out_y):
        result = True

    elif (fan_out_x == fan_out_y):
        if (fan_in_x > fan_in_y):
            result = True

        elif (fan_in_x == fan_in_y):
            if(arc_x > arc_y):
                result = True

    return result
