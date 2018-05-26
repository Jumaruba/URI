def const_matriz():
    matriz = []
    zeros = 0
    for i in range(3):
        x = list(map(int, input().split()))
        zeros += x.count(0)
        matriz.append(x)
    return matriz, zeros


def soma_linha(matriz):
    for i in range(3):
        if 0 not in matriz[i]:
            return sum(matriz[i])
    return 0


def soma_coluna(matriz):
    for coluna in range(3):
        detector = 0
        soma = 0
        for linha in range(3):
            if matriz[linha][coluna] == 0:
                detector = 1
            soma += matriz[linha][coluna]
        if detector == 0:
            return soma
    return 0


def soma_digaonal_direita(matriz):
    soma = 0
    for linha in range(3):
        soma += matriz[linha][linha]
        if matriz[linha][linha] == 0:
            return 0
    return soma


def soma_diagonal_esquerda(matriz):
    soma = 0
    for linha in range(3):
        soma += matriz[linha][-linha - 1]
    return soma


def completando_linha(matriz, soma):
    for i in range(3):
        vezes = matriz[i].count(0)
        if vezes == 1:
            index = matriz[i].index(0)
            soma_linha = sum(matriz[i])
            matriz[i][index] = soma - soma_linha
    return matriz


def completando_coluna(matriz, soma):
    for coluna in range(3):
        zero = 0
        soma_momento = 0
        for linha in range(3):
            soma_momento += matriz[linha][coluna]
            if matriz[linha][coluna] == 0:
                zero += 1
                index = linha
        if zero == 1:
            matriz[index][coluna] = soma - soma_momento
    return matriz


matriz, zeros = const_matriz()

soma = soma_linha(matriz)

if soma == 0:
    soma = soma_coluna(matriz)

    if soma == 0:
        soma = soma_digaonal_direita(matriz)

        if soma == 0:
            soma = soma_diagonal_esquerda(matriz)

print(soma)
matriz = completando_linha(matriz, soma)
matriz = completando_coluna(matriz, soma)

for linha in range(3):
    for coluna in range(2):
        print(matriz[linha][coluna], end=' ')
    print(matriz[linha][2])
