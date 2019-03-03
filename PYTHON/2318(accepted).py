def soma_linhas():
    for j in range(x):
        if 0 not in matriz[j]:
            return sum(matriz[j])
    return 0


def soma_coluna():
    for j in range(x):
        aux = []
        for m in range(x):
            aux.append(matriz[m][j])
        if 0 not in aux:
            return sum(aux)
    return 0


def soma_diagonal():
    s = 0
    for j in range(x):
        if matriz[j][j] != 0:
            s += matriz[j][j]
        else:
            return 0
    return s


def soma_diagonal_s():
    s = 0
    for j in range(x):
        if matriz[j][-1 - j]:
            s += matriz[j][-1 - j]
        else:
            return 0
    return s


def consert_linha():
    for j in range(x):
        if matriz[j].count(0) == 1:
            matriz[j][matriz[j].index(0)] = soma - sum(matriz[j])
    return matriz


def consert_coluna():
    for j in range(x):
        aux = []
        for m in range(x):
            aux.append(matriz[m][j])
        if aux.count(0) == 1:
            matriz[aux.index(0)][j] = soma - sum(aux)
    return matriz


x = 3

matriz = [list(map(int, input().split())) for i in range(x)]
soma = soma_linhas()
if not soma:
    soma = soma_coluna()
    if not soma:
        soma = soma_diagonal()
        if not soma:
            soma = soma_diagonal_s()
            if not soma:
                for k in range(3):
                    soma += sum(matriz[k])
                soma //= 2

matriz = consert_linha()
matriz = consert_coluna()
for k in range(x):
    print(*matriz[k])
