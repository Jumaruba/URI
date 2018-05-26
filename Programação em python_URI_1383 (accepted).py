quantidade = int(input())


def matrizes(metrica):
    lista = []
    for k in range(9):
        x = list(map(int, input().split()))
        lista.append(x)
        k = x[:]
        k.sort()
        if k != metrica:
            return -1
    return lista


def checa_colunas(metrica, matriz):
    for coluna in range(0, 9):
        lista = []
        for linha in range(0, 9):
            lista.append(matriz[linha][coluna])
        k = lista[:]
        k.sort()
        if k != metrica:
            return -1
    return True


def quadrado(linha, coluna, matriz, metrica):
    lista = []
    for i in range(linha, linha + 3):
        for j in range(coluna, coluna + 3):
            lista.append(matriz[i][j])
    k = lista[:]
    k.sort()

    if metrica != k:
        return -1
    return 2


def main():
    metrica = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    matriz = matrizes(metrica)

    if matriz == -1:
        return False
    else:
        verdade = checa_colunas(metrica, matriz)
        if verdade == -1:
            return False
        else:
            for linha in range(0, 7, 3):
                for coluna in range(0, 7, 3):
                    verdade = quadrado(linha, coluna, matriz, metrica)
                    if verdade == -1:
                        return False
            return True

for i in range(quantidade):
    bolena = main()
    print('Instancia %i' % (i + 1))
    if bolena:
        print('SIM')
    else:
        print('NAO')
    print('')
