def matriz_inicio(quantidade):
    for i in range(quantidade):
        matriz.append([])
    return matriz

def matriz_fim(linhas, matriz):
    for i in range(linhas):
        x = list(map(int,input().split()))
        matriz[x[0]-1] += [x[1]]
        matriz[x[1]-1] += [x[0]]
    return matriz

def profundidade(n,marcado):
    marcado.append(n)
    for i in matriz[n-1]:
        if i not in marcado:
            profundidade(i,marcado)
    return marcado

marcado = []
matriz = []
quantidade, linhas = map(int, input().split())
while True:
    try:
        matriz = matriz_inicio(quantidade)
        matriz = matriz_fim(linhas,matriz)
        n = int(input())
        marcado = profundidade(n,marcado)

        print(len(marcado))
        quantidade, linhas = map(int, input().split())
        marcado = []
        matriz = []

    except EOFError:
        break
