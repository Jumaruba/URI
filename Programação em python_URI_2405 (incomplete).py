def const_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz


def algoritmo_torre(matriz, x, y):
    numero_vert_pos = 0
    contador = 1
    while numero_vert_pos != 1:  # vertical positiva
        numero_vert_pos = matriz[x][y + contador]
        if numero_vert_pos != 1:
            matriz[x][y + contador] = 1
            contador += 1
    total = contador
    print(total, contador)

    numero_vert_neg = 0
    contador = 1
    while numero_vert_neg != 1:  # vertical negativa
        numero_vert_neg = matriz[x][y - contador]
        if numero_vert_neg != 1:
            matriz[x][y - contador] = 1
            contador += 1

    total += contador - 1
    print(total,contador)

    contador = 1
    numero_hor_pos = 0
    while numero_hor_pos != 1:  # horizontal positiva
        numero_hor_pos = matriz[x + contador][y]
        if numero_hor_pos != 1:
            matriz[x + contador][y] = 1

    total += contador - 1
    print(total, contador)

    contador = 1
    numero_hor_neg = 0
    while numero_hor_neg != 1:  # horizontal positiva
        numero_hor_neg = matriz[x - contador][y]
        if numero_hor_neg != 1:
            matriz[x - contador][y] = 1

    total += contador - 1
    print(total, contador)
    return total


linhas, colunas, x, y, quantidade = map(int, input().split())

matriz = const_matriz(linhas, colunas)
contador = 1

for k in range(quantidade):
    linha, coluna = map(int, input().split())
    matriz[linha - 1][coluna - 1] = 1

print(algoritmo_torre(matriz, x, y))
