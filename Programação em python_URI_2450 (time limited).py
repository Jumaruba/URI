linha, coluna = map(int, input().split())


def const_metrica(coluna):  # linha completa de zero
    metrica = []
    for i in range(coluna):
        metrica.append(0)
    return metrica


def const_matriz(linha):  # construindo a matriz
    matriz = []
    for i in range(linha):
        x = list(map(int, input().split()))
        matriz.append(x)
    return matriz


def linhas_abaixo(linha_pos, linha, metrica, matriz):  # caso a linha seja toda zero
    for i in range(linha_pos, linha):
        if matriz[i] != metrica:
            return False
    return True


def dif_zero(linha_pos, coluna_pos, matriz, linha):  # caso a linha nao tenha apenas zeros
    if coluna_pos - 1 >= 0:
        for k in range(linha_pos + 1, linha):
            for m in range(coluna_pos, -1, -1):
                if matriz[k][m] != 0:
                    return False
    return True


def analise(linha, coluna, matriz, metrica):
    for linha_pos in range(linha):
        if matriz[linha_pos] == metrica:
            quero = linhas_abaixo(linha_pos, linha, metrica, matriz)
            if quero == False:
                return quero
        else:
            coluna_pos = -1
            while coluna_pos == -1 or matriz[linha_pos][coluna_pos] == 0:
                coluna_pos += 1
                if matriz[linha_pos][coluna_pos] != 0:
                    quero = dif_zero(linha_pos, coluna_pos, matriz, linha)
                    if quero == False:
                        return quero

    return True


def main():
    metrica = const_metrica(coluna)
    matriz = const_matriz(linha)
    boleana = analise(linha, coluna, matriz, metrica)
    if boleana:
        print('S')
    else:
        print('N')


main()
