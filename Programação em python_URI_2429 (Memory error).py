x = int(input())


def busca(inicio, grafo):
    status = [0] * x
    fila = [inicio]
    while fila != [] and 0 in status:
        v = fila.pop()
        for z in range(x):
            if grafo[v][z] == 1 and status[z] == 0:
                status[z] = 1
                fila.append(z)
    return 0 in status


grafo = [[0 for i in range(x)] for j in range(x)]

for m in range(x):
    w, y = map(int, input().split())
    grafo[w - 1][y - 1] = 1

if busca(0, grafo):
    print('N')
else:
    print('S')
