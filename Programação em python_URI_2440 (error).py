def busca(grafo, inicio, status):
    fila = [inicio]
    while fila != [] and 0 in status:
        v = fila.pop()
        status[v] = 1
        for w in range(nvertices):
            if grafo[v][w] == 1 and status[w] == 0:
                fila.append(w)
                status[w] = 1
    return status


elementos, linhas = map(int, input().split())
grafo = [[0 for k in range(elementos)] for m in range(elementos)]

for i in range(linhas):
    x, y = map(int, input().split())
    grafo[x - 1][y - 1] = 1
    grafo[y - 1][x - 1] = 1

nvertices = len(grafo)
status = [0] * nvertices
fam = 0
while 0 in status:
    i = status.index(min(status))
    fam += 1
    status = busca(grafo, i, status)

print(fam)
