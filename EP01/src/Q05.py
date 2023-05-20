import networkx as nx

def valid_word(g, s, t, w):
    
    #Verifica se algum dos parâmetros é vazio.
    if (g == None or s == None or t == None or w == None):
        return None
    
    #Verifica se os vértices do parâmetro estão no grafo.
    if ( (not g.__contains__(s)) or  ( not g.__contains__(t)) ):
        return None 
    
    #Verifica se o arco inicial é o mesmo que o final.
    if not s == t:
        
        #Captura todos os caminhos possíveis entre o arco inicial e o final.
        paths = list(nx.all_simple_paths(g, s, t))
        
        saida = ""
        #Percorre toda a lista de caminhos.
        for caminho in paths:
            
            #Percorre todos os vértices do caminho
            for i in range(0, len(caminho) - 1):
                
                #Verifica se as arestas possuem label
                tem_label = verifica_se_arestas_possuem_label(g, i)
                if (tem_label == False):
                    return None
                
                #Verifica se o vértice g[i] possui uma aresta loop
                if (i in g[i]):
                    letra = str(g[i][i][0])[11]
                    #Quantas vezes o label desse loop está na palavra w
                    count = calcula_ocorrencias(w, saida, letra)
                    #Percorre a aresta loop inserindo o label da aresta na variável saida        
                    while ( count > 0):
                        saida += letra
                        count -= 1
                
                #Captura o label da aresta [i][i+1]
                letra = str(g[i][i+1][0])[11]
                
                #Verifica se o label dessa aresta está na palavra w
                count = calcula_ocorrencias(w, saida, letra)
                #Caso esteja, então esse label é inserido na variável saida
                if ( count >= 0 ):
                    saida += letra
                    
            #Se saida for igual a W, então a palavra foi formada
            #O slice é necessário, para evitar problemas com a aresta de número 0
            if (saida == w or saida[1:] == w):
                return True
            
            #Reinicia a variável saida, para o próximo caminho que será percorrido
            else:
                saida = ""
                
        return False
              
    #Verifica se a palavra é uma String vazia, caso seja, há como formá-la no grafo.
    if (w == ""):
        return True
    else:
        return False
    

#Calcula a quantidade de vezes que o label ocorre na palavra que veio do parâmetro
#A comparação com a quantidade de vezes em que esse label já foi inserido na variável de saida,
#é necessária para os casos em que esse label é de uma aresta loop    
def calcula_ocorrencias(entrada, saida, letra):
    count_entrada = 0
    for char in entrada:
        if char == letra:
            count_entrada += 1
            
    count_saida = 0
    for char in saida:
        if char == letra:
            count_saida += 1
            
    return (count_entrada - count_saida)


#Verifica se o grafo possui labels em suas arestas
def verifica_se_arestas_possuem_label(g, i):
    tem_label_arestas = len(str(g[i][i+1][0]))
    if (tem_label_arestas < 3):
        return False
    