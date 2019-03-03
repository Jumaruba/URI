def const_matriz(matrix):
    for r in range(x):
        if sum(matrix[r]) != ss or len(set(matrix[r])) != len(matrix[r]):
            return False
    return True


def checa_coluna(soma):
    for j in range(x):
        aux = []
        for k in range(x):
            aux.append(matriz[k][j])
        if sum(aux) != soma:
            return False
    return True


def checa_diagonal(soma):
    s = 0
    for v in range(x):
        s += matriz[v][v]
    if s == soma:
        return True
    return False


def checa_diagonal_s(soma):
    s = 0
    for w in range(x):
        s += matriz[w][-w - 1]
    if s == soma:
        return True
    return False


x = int(input())
matriz = [list(map(int, input().split())) for q in range(x)]
ss = sum(matriz[0])
bol = const_matriz(matriz)
if not bol:
    print(0)
else:
    bol = checa_coluna(ss)
    if bol:
        bol = checa_diagonal(ss)
        if bol:
            bol = checa_diagonal_s(ss)
            if bol:
                print(ss)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
