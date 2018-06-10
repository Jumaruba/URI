def busca_em_largura(grafo, inicio):
    nvertices = len(grafo)

    # Variaveis contendo dados sobre o andamento da função
    status = [0] * nvertices
    fila = [inicio]
    status[inicio] = 1

    while fila != [] and 0 in status:
        v = fila.pop()
        for w in range(nvertices):
            if grafo[v][w] == 1 and status[w] == 0:
                status[w] = 1
                fila.append(w)
    return 0 not in status


e, l = map(int, input().split())
teste_n = 0
while e != 0 and l != 0:
    teste_n += 1
    grafo = [[0 for j in range(e)] for k in range(e)]
    for i in range(l):
        x, y = map(int, input().split())
        grafo[x-1][y-1] = 1
        grafo[y-1][x-1] = 1
    print('Teste {}'.format(teste_n))
    if busca_em_largura(grafo, 1):
        print('normal')
    else:
        print('falha')
    print('')
    e, l = map(int, input().split())