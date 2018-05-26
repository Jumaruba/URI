linhas, colunas, l, c = map(int, input().split())

matriz = []

for i in range(0, linhas):
    for j in range(0, colunas):
        aux_matriz = list(map(int, input().split()))
        matriz.append(aux_matriz)

