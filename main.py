from grafo import *

def valida_Aresta(arestas):
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

def valida_Vertice(vertice):

    if not Grafo.verticeValido(vertice):
        print('Vértices inválidos. Informe vértices Válidos!')
        return True

    elif vertice.isspace():
        print('Erro 0')
        return True

def grafo_Completo(Vertices, nome_arestas):
    conj_vertNaoAdj = []
    for vert1 in Vertices:
        for vert2 in Vertices:
            if (vert1 + '-' + vert2) not in nome_arestas and (vert2 + '-' + vert1) not in nome_arestas and vert1 != vert2 \
                    and (vert1,vert2) not in conj_vertNaoAdj and (vert2,vert1) not in conj_vertNaoAdj:
                conj_vertNaoAdj.append((vert1, vert2))
    if len(conj_vertNaoAdj) == 0:
        return True
    else:
        return False

def laco(vertice,conjuntoDict_Arestas): #verifica a existencia de laços
    chaves = conjuntoDict_Arestas.keys()
    for nome in chaves:
        if vertice+'-'+vertice == conjuntoDict_Arestas[nome]:
            return True
    return False

def exist_Aresta_Paralela(nome_arestas):
    for aresta1 in nome_arestas:
        for aresta2 in nome_arestas:
            if aresta1 != aresta2 and aresta1 == aresta2[-1]+'-'+aresta2[0]:
                return True
    return False

def grau_vertice(vert, nome_arestas):
    grau = 0
    for aresta in nome_arestas:
        if vert in aresta:
            grau +=1
    return grau

def vert_NaoAdjacentes(Vertices, nome_arestas):
    conj_vertNaoAdj = []
    for vert1 in Vertices:
        for vert2 in Vertices:
            if (vert1 + '-' + vert2) not in nome_arestas and (vert2 + '-' + vert1) not in nome_arestas and vert1 != vert2 \
                    and (vert1,vert2) not in conj_vertNaoAdj and (vert2,vert1) not in conj_vertNaoAdj:
                conj_vertNaoAdj.append((vert1, vert2))
    return conj_vertNaoAdj

def arestas_Sobre_Vertices(vertice,chaves):
    conj_arestas_Sobre_Vertices = []
    for chave in chaves:
        if conjuntoDict_Arestas[chave][0] == vertice or conjuntoDict_Arestas[chave][-1] == vertice:
            conj_arestas_Sobre_Vertices.append(chave)
    return conj_arestas_Sobre_Vertices

cont = 0
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
        if valida_Vertice(vertice):
            cont = 0
            break

    if cont == len(Vertices):
        cont = 0
        parada = False

while parada == False:
    arestas = input('Informe as arestas separados por vírgulas(Exemplo: a1(b-c),a2(c-d),...): ')

    conjuntoDict_Arestas = valida_Aresta(arestas)
    try:
        grafo_Valido = Grafo(Vertices, conjuntoDict_Arestas)
    except:
        print("Arestas inválidas: Verifique se os vértice informados estão definidos. Informe as arestas novamente.")
        continue

    chaves = conjuntoDict_Arestas.keys()

    for nome in chaves:
        cont += 1
        if nome.isspace() or nome == '':
            cont = 0
            print('Nome de aresta inválida. Informe as arestas no formato a1(b-c),a2(c-d),... ')
            continue

    if cont == len(conjuntoDict_Arestas):
        parada = True

nome_arestas = [] #conjunto das arestas
chaves = conjuntoDict_Arestas.keys() #conjunto das chaves

for chave in chaves:
    nome_arestas.append(conjuntoDict_Arestas[chave])

print(grafo_Completo(Vertices,nome_arestas))