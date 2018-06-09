def linhas(matriz):
    for i in range(3):
        x = matriz[i].count(0)
        if x == 0:
            return sum(matriz[i])
    return 0


def colunas(matriz):
    for colunas in range(3):
        aux = []
        for linhas in range(3):
            if matriz[linhas][colunas] != 0:
                aux.append(matriz[linhas][colunas])
        if len(aux) == 3:
            return sum(aux)
    return 0


def diagonal_p(matriz):
    soma = 0
    for i in range(3):
        if matriz[i][i] != 0:
            soma += matriz[i][i]
        else:
            return 0
    return soma

def diagonal_s(matriz):
    soma = 0
    for i in range(3):
        soma+= matriz[i][-i-1]
    return soma


def pre_linhas(matriz, soma):
    for i in range(3):
        x = matriz[i].count(0)
        if x == 1:
            matriz[i][matriz[i].index(0)] = soma - sum(matriz[i])
    return matriz


def pre_colunas(matriz, soma):
    for colunas in range(3):
        aux = []
        for linhas in range(3):
            aux.append(matriz[linhas][colunas])
        if aux.count(0) == 1:
            matriz[aux.index(0)][colunas] = soma - sum(aux)
    return matriz


matrix = [list(map(int, input().split())) for j in range(3)]
soma = linhas(matrix)
if soma == 0:
    soma = colunas(matrix)
    if soma==0:
        soma = diagonal_p(matrix)
        if soma==0:
            soma = diagonal_s(matrix)
            matrix = pre_linhas(matrix, soma)
            matrix = pre_colunas(matrix, soma)
        else:
            matrix = pre_linhas(matrix, soma)
            matrix = pre_colunas(matrix, soma)
    else:
        matrix = pre_linhas(matrix, soma)
        matrix = pre_colunas(matrix, soma)
else:
    matrix = pre_linhas(matrix, soma)
    matrix = pre_colunas(matrix, soma)

for k in range(3):
    for m in range(2):
        print(matrix[k][m], end=' ')
    print(matrix[k][2])
