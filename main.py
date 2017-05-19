from grafo import *

def trataAresta(arestas):
    lista_Aresta = []
    lista_aux1 = arestas.split(', ')
    arestas_dict = {}
    for i in lista_aux1:
        lista_Aresta.append(i.split('('))
    for j in range(len(lista_Aresta)):
        if lista_Aresta[j][1].count(')') != 0: # Sem esse if da erro no raplace
            lista_Aresta[j][1] = lista_Aresta[j][1].replace(')','')
    for k in lista_Aresta:
        arestas_dict[k[0]] = k[1]
    return arestas_dict

cont = 0
SEPARADOR_ARESTA = '-'
parada = True
arestas_validas = {}
Vertices = []

while parada == True:
    vert = input('Informe os vértices separados por vírgulas: ')

    if vert.count('(') != vert.count(')') != 0:
        print('Vértices invalidos. Informe vértices sem parênteses!')
        continue

    Vertices = vert.split(',')

    for vertice in Vertices:
        cont += 1
        if not Grafo.verticeValido(vertice):
           print('Vértices inválidos. Informe vértices Válidos!')
           cont = 0 # cont recebe 0 para reiniciar a contagem
           break

        elif vertice.isspace():
            print('Erro 0')
            cont = 0
            break

    if cont == len(Vertices):
        cont = 0
        parada = False

while parada == False:
    arestas = input('Informe as arestas separados por vírgulas(Exemplo: a1(b-c),a2(c-d),...): ')

    conjuntoDict_Arestas = trataAresta(arestas)

    for chave in conjuntoDict_Arestas.keys():
        cont += 1

        if conjuntoDict_Arestas[chave].isspace():
            print('Erro 0: A aresta',conjuntoDict_Arestas[chave],'não é válida. Informe novamente as arestas a partir da aresta', conjuntoDict_Arestas[chave],'!')
            cont = 0
            break

        elif not Grafo.arestaValida(Grafo,conjuntoDict_Arestas[chave]): #Erro pede outro argumento self
           print('Erro 1: A aresta',conjuntoDict_Arestas[chave],'não é válida. Informe novamente as arestas a partir da aresta', conjuntoDict_Arestas[chave],'!')
           cont = 0
           break

        elif chave.count(SEPARADOR_ARESTA) != 0:
            print('Erro 2: A aresta',conjuntoDict_Arestas[chave],'não é válida. Informe novamente as arestas a partir da aresta', conjuntoDict_Arestas[chave],'!')
            cont = 0
            break

        elif conjuntoDict_Arestas[chave].count('(') != 0 or conjuntoDict_Arestas[chave].count(')') != 0:
            print('Erro 3: A aresta',conjuntoDict_Arestas[chave],'não é válida. Informe novamente as arestas a partir da aresta', conjuntoDict_Arestas[chave],'!')
            cont = 0
            break

        elif conjuntoDict_Arestas[chave][0] == SEPARADOR_ARESTA:
            print('Erro 4: A aresta',conjuntoDict_Arestas[chave],'não é válida. Informe novamente as arestas a partir da aresta', conjuntoDict_Arestas[chave],'!')
            cont = 0
            break

        elif conjuntoDict_Arestas[chave][-1] == SEPARADOR_ARESTA:
            print('Erro 5: A aresta',conjuntoDict_Arestas[chave],'não é válida. Informe novamente as arestas a partir da aresta', conjuntoDict_Arestas[chave],'!')
            cont = 0
            break

        arestas_validas[chave] = conjuntoDict_Arestas[chave] # Se a aresta salva

    if cont == len(conjuntoDict_Arestas):
        parada = True

test_grafo = Grafo(Vertices,arestas_validas)
print(test_grafo)
