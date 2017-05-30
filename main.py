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
    for i in range(len(lista_Aresta)): # verifica se tem Nome de arestas repetidas(Chaves Repetidas)
        if i + 1 < len(lista_Aresta):
            if lista_Aresta[i][0] == lista_Aresta[i+1][0]:
                return False
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
    for vert1 in Vertices:
        for vert2 in Vertices:
            if (vert1 + '-' + vert2) not in nome_arestas and (vert2 + '-' + vert1) not in nome_arestas and vert1 != vert2:
                return False
    return True

def laco(vertice,conjuntoDict_Arestas): #verifica a existencia de laços
    chaves = conjuntoDict_Arestas.keys()
    for nome in chaves:
        if vertice+'-'+vertice == conjuntoDict_Arestas[nome]:
            return True
    return False

def exist_Aresta_Paralela(nome_arestas):
    for aresta1 in nome_arestas:
        for aresta2 in nome_arestas:
            i_traco = aresta2.index(SEPARADOR_ARESTA)
            if aresta1 != aresta2 and aresta1 == aresta2[i_traco+1:]+'-'+aresta2[:i_traco]:
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
        i_traco = conjuntoDict_Arestas[chave].index(SEPARADOR_ARESTA)
        if conjuntoDict_Arestas[chave][:i_traco] == vertice or conjuntoDict_Arestas[chave][i_traco+1:] == vertice:
            conj_arestas_Sobre_Vertices.append(chave)
    return conj_arestas_Sobre_Vertices

cont = 0
parada = True
Vertices = []
nome_arestas = []
SEPARADOR_ARESTA = '-'

while parada == True:
    vert = input('Informe os vértices separados por vírgulas: ')

    if vert.count('(') != 0 or vert.count(')') != 0 or vert[-1].isspace() is True or vert[-1]==',':
        print('Vértices invalidos. Informe vértices válidos!')
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
    if conjuntoDict_Arestas is False:
        print('Existem nomes de arestas repetidas. Informe novamente as arestas.')
        continue
    try:
        grafo_Valido = Grafo(Vertices, conjuntoDict_Arestas)
    except:
        print('Arestas inválidas: Verifique se os vértice informados estão definidos. Informe as arestas novamente.')
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

for chave in chaves:
    nome_arestas.append(conjuntoDict_Arestas[chave])

def __Aux1_ciclo(vertice,arestas): #retorna o ultimo vertice EX: AS-DF essa função retorna DF.
    for i in arestas:
        i_traco = i.index(SEPARADOR_ARESTA)
        if vertice not in i: # evita esse caso f(a-d),g(s-a),h(a-s)
            continue

        if vertice == i[:i_traco]:
            return i[i_traco+1:]

def ciclo(Vertice,nome_arestas,lista=[], cont = 0):  #Cria um ciclo
    lista.append(Vertice)
    proximo_vertice = __Aux1_ciclo(Vertice, nome_arestas)
    while True:
        cont += 1
        if cont == len(Vertices):
            break
        lista.append(proximo_vertice)
        if lista[0] == lista[-1]:
            return lista
        proximo_vertice = __Aux1_ciclo(proximo_vertice, nome_arestas)
    return lista

print(ciclo('a',nome_arestas, lista = []))
print(ciclo('d',nome_arestas, lista=[]))

'''def ciclos(Vertices, nome_arestas, conjunto_Ciclos = [], cont = 0):
    adiciona = True
    for vertice in Vertices:
        ciclo = __Aux1_ciclo(vertice,nome_arestas,lista=[])
        if len(conjunto_Ciclos) != 0:
            for i in conjunto_Ciclos:
                for j in range(len(ciclo)):
                    print(ciclo[j])
                    print(i)
                    if ciclo[j] in i:
                        cont += 1
                    if cont == len(i):
                        adiciona = False

        if ciclo[0] == ciclo[-1] and adiciona:
            conjunto_Ciclos.append(ciclo)
    return conjunto_Ciclos



print(ciclos(Vertices,nome_arestas))'''

# a, s, d, f, g
# q(a-s),w(s-d),e(d-a),r(d-f),t(f-g),y(g-d) para o a