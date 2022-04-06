from collections import deque
dist = {}

def bfs(G, s):
    cor = {}
    dist = {}
    pred = {}

    for vertice in G.keys():
        cor[vertice], dist[vertice], pred[vertice] = 'branco', -1, None
    cor[s] = 'cinza'
    dist[s] = 0

    Q = deque([s])
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if cor[v] == 'branco':
                cor[v], dist[v], pred[v] = 'cinza', dist[u] + 1, u
                Q.append(v)
        cor[u] = 'preto'
    return dist, pred


def print_path(pred, orig, dest):
    if orig == dest:
        print("você chegou a origem que é: " + orig)
    else:
        if pred[dest] == None:
            print('Sem caminho')
        else:
            print("predecessor do {} é: {}".format(dest, pred[dest]))
            print("e a distancia de {} até {} é: {}".format(dest, orig, dist[dest]))
            print_path(pred, orig, pred[dest])


G = {
    '1': ['3', '5'],
    '2': ['7', '4'],
    '3': ['8'],
    '4': ['1'],
    '5': ['2', '4'],
    '6': ['4', '9'],
    '7': ['6'],
    '8': ['5'],
    '9': ['1'],
}

dist, pred = bfs(G, '1')
print_path(pred, '1', '9')