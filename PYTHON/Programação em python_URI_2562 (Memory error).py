def busca(grafo, inicio):
    nvertices = len(grafo)
    status = [0] * nvertices
    fila = [inicio - 1]
    status[inicio - 1] = 1

    while fila != [] and 0 in status:
        v = fila.pop()
        for w in range(nvertices):
            if grafo[v][w] == 1 and status[w] == 0:
                fila.append(w)
                status[w] = 1
    return status.count(1)


while True:
    try:
        vertices, linhas = map(int, input().split())
        grafo = [[0 for i in range(vertices)] for j in range(vertices)]
        for k in range(linhas):
            x, y = map(int, input().split())
            grafo[x - 1][y - 1] = 1
            grafo[y - 1][x - 1] = 1
        inicio = int(input())
        print(busca(grafo, inicio))

    except EOFError:
        break
