from grafo import *

def trataAresta(arestas):
    lista_Aresta = []
    lista_aux1 = arestas.split(',')
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
Vertices = []
grafo_Valido = []

while parada == True:
    vert = input('Informe os vértices separados por vírgulas: ')

    if vert.count('(') != 0 or vert.count(')') != 0:
        print('Vértices invalidos. Informe vértices sem parênteses!')
        continue

    Vertices = vert.split(', ')

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
    try:
        grafo_Valido = Grafo(Vertices, conjuntoDict_Arestas)
        break
    except:
        print("Arestas inválidas. Verifique se os vértice informados nas aresta condizem com os vértices informados. Informe as arestas novamente.")
        continue
print(grafo_Valido)
