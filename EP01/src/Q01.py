import networkx as nx


# Elementos da lista: (name, surname, country)
def associate_astronauts(list_a):
    
    #Verifica se a lista é vazia 
    if (list_a is None):
        return None
    
    # Criação do grafo
    G = nx.Graph()
    
    # Adição dos nodes e atributos
    n = 0
    for astronauta in list_a:
        if (type(astronauta) == int or len(astronauta) < 3):
            return None
        
        name = astronauta[0]
        surname = astronauta[1]
        nacionalidade = astronauta[2]
        G.add_node(n, firstName=name, lastName=surname, country=nacionalidade)
        n += 1
            
    # Combinação de nodes, para criação de edges (duplas) com nacionalidades diferentes
    for j in range(len(G.nodes)):
        nacionalidade_1 = nx.get_node_attributes(G, "country")
        nome_1 = nx.get_node_attributes(G, "firstName")
        for i in range(len(G.nodes)):
            nacionalidade_2 = nx.get_node_attributes(G, "country")
            nome_2 = nx.get_node_attributes(G, "firstName")
            if (nacionalidade_1[j] != nacionalidade_2[i] and nome_1[j] != nome_2[i]):
                G.add_edge(j, i)
    
    #Retorno do grafo com a adição de seus edges e nodes, seguindo a especificação da questão.
    return G
