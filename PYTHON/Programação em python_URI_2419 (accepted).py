def costa(matriz, index_linha, index_coluna):  # costas nao laterais
    if matriz[index_linha][index_coluna] == '#':
        if matriz[index_linha - 1][index_coluna] == '.' or matriz[index_linha + 1][index_coluna] == '.':
            return 1
        elif matriz[index_linha][index_coluna - 1] == '.' or matriz[index_linha][index_coluna + 1] == '.':
            return 1
        else:
            return 0
    else:
        return 0


def Const_matriz(linha):  # criando a matriz
    matriz = []
    for i in range(linha):
        n = list(input())
        matriz.append(n)
    return matriz


def costa_lateral(matriz, linha, coluna):  # costas lalterais
    quantidade = matriz[0].count('#')
    quantidade += matriz[linha - 1].count('#')
    for i in range(1, linha - 1):
        if matriz[i][0] == '#':
            quantidade += 1
        if matriz[i][coluna - 1] == '#':
            quantidade += 1
    return quantidade


linha, coluna = map(int, input().split())

matriz = Const_matriz(linha)

quantidade = costa_lateral(matriz, linha, coluna)

for i in range(1, linha - 1):
    for j in range(1, coluna - 1):
        quantidade += costa(matriz, i, j)

print(quantidade)
