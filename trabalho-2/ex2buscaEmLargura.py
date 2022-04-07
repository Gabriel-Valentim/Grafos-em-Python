from collections import deque
dist = {}

def contaSubGrafos(G, s):
    cor = {}
    dist = {}
    pred = {}
    posIn = {}

    cont = 0 

    for vertice in G.keys():
        cor[vertice], dist[vertice], pred[vertice] = 'branco', -1, None
    cor[s] = 'cinza'
    dist[s] = 0

    for vert in G.keys():
        Q = deque([vert])
        if dist[vert] == -1 or cont == 0:
            posIn[cont] = vert
            cont += 1
        while len(Q) > 0:
            u = Q.popleft()
            for v in G[u]:
                if cor[v] == 'branco':
                    cor[v], dist[v], pred[v] = 'cinza', dist[u] + 1, u
                    Q.append(v)
            cor[u] = 'preto'

    return cont, posIn

def bfs(G, s):
    cor = {}
    dist = {}
    pred = {}
    grafos = {}

    cont = 0

    for vertice in G.keys():
        cor[vertice], dist[vertice], pred[vertice] = 'branco', -1, None
    cor[s] = 'cinza'
    dist[s] = 0

    Q = deque([s])
    grafos[cont] = s
    while len(Q) > 0:
        cont += 1
        u = Q.popleft()
        if cont >= 2:
            grafos[cont] = u
        for v in G[u]:
            if cor[v] == 'branco':
                cor[v], dist[v], pred[v] = 'cinza', dist[u] + 1, u
                Q.append(v)
        cor[u] = 'preto'
    print(grafos)
    return dist, pred


G = {
    '1': ['2'],
    '2': ['1'],
    '3': ['4', '6'],
    '4': ['3', '5'],
    '5': ['4', '6'],
    '6': ['5', '3'],
    '7': ['8', '9'],
    '8': ['7', '9'],
    '9': ['7', '8'],
    '10': ['11'],
    '11': ['10'],
    '12': ['13', '14'],
    '13': ['12', '14'],
    '14': ['12', '13'],
}

cont, posIn = contaSubGrafos(G, '1')

print("Esse grafo possui {} sub-grafos, são eles".format(cont))
for i in range(0,cont):
    dist, pred = bfs(G, posIn[i])
