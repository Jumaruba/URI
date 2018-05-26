def mat():
    global n
    matriz = []
    for i in range(n):
        k = list(map(int, input().split()))  # colocando os termos da matriz
        matriz.append(k)
    for m in range(n):
        for j in range(n):
            matriz[m][j] = int(matriz[m][j]) * int(matriz[m][j])
    return matriz


def maior_da_coluna(matriz):
    lista = []
    for coluna in range(n):
        maior = 0
        for linha in range(n):
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
        maior = str(maior)
        lista.append(len(maior))
    return lista


def ajustando(matriz, lista):
    for coluna in range(n):
        for linha in range(n):
            algarismos = len(str(matriz[linha][coluna]))
            espacos = lista[coluna] - algarismos
            matriz[linha][coluna] = str(' ' * espacos) + str(matriz[linha][coluna])
    return matriz


quantidade = int(input())
contador = 4
for i in range(quantidade):
    n = int(input())
    matriz = mat()
    lista = maior_da_coluna(matriz)
    matriz = ajustando(matriz, lista)
    print('Quadrado da matriz #%i:' % contador)
    for j in range(0, n):
        for z in range(0, n - 1):
            print(matriz[j][z], end=' ')
        print(matriz[j][n - 1])
    contador += 1
    if i != quantidade - 1:
        print('')


# ainda contem erros de apresentação, por isso não está certo
