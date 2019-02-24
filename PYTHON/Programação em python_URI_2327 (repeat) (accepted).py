def linhas(matrix, ss):
    for z in range(x):
        if sum(matrix[z]) != ss:
            return False
    return True


def colunas(matrix, ss):
    for m in range(x):
        aux = []
        for n in range(x):
            aux.append(matrix[n][m])
        if sum(aux) != ss:
            return False
    return True


def diag_p(matrix, ss):
    p = 0
    for m in range(x):
        p += matrix[m][m]
    if p != ss:
        return False
    return True


def diag_s(matrix, ss):
    p = 0
    for m in range(x):
        p += matrix[m][-1 - m]
    if p != ss:
        return False
    return True


x = int(input())

matriz = [list(map(int, input().split())) for i in range(x)]
soma = sum(matriz[0])
bol = linhas(matriz, soma)
if bol:
    bol = colunas(matriz, soma)
    if bol:
        bol = diag_p(matriz, soma)
        if bol:
            bol = diag_s(matriz, soma)
            if bol:
                print(soma)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)
else:
    print(-1)
